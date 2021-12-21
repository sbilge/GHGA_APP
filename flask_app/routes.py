from flask import render_template, request, make_response
from flask_app import app, db
from flask_app.models import Study, Sample, Experiment, File
from sqlalchemy.exc import IntegrityError



# create database tables before the first request, if they do not initially exist
@app.before_first_request
def create_metadata_tables():
    db.create_all()


# Populate database with metadata
@app.route('/metadata', methods = ['POST'])
def add_study():
    # Receive metadata as json from the client
    metadata = request.get_json()

    # Create Study object and add to the study table
    name = metadata['name']
    description = metadata['description']

    new_study = Study(name = name, description = description)

    try:
        db.session.add(new_study)
        # Parse json to create database entries

        # Create Sample objects and add to the sample table
        for sample in metadata['sample']:
            donor_age = sample['donor_age']
            donor_sex = sample['donor_sex']
            tissue_type = sample['tissue_type']

            new_sample = Sample(donor_age = donor_age, donor_sex = donor_sex, tissue_type = tissue_type)
            
            new_study.samples.append(new_sample)

            db.session.add(new_sample)


            # Create Experiment objects and add to the experiment table
            for experiment in sample['experiment']:
                experiment_type = experiment['experiment_type']

                new_experiment = Experiment(experiment_type = experiment_type)
                
                new_sample.experiments.append(new_experiment)

                db.session.add(new_experiment)


                # Create File objects and add to the file table
                for file in experiment['file']:
                    file_name = file['file_name']
                    file_size = file['size']
                    checksum = file['checksum']

                    new_file = File(file_name = file_name, file_size = file_size, checksum = checksum)
                    
                    new_experiment.files.append(new_file)

                    db.session.add(new_file)

        db.session.commit()
    
        return make_response(f"metadata of {new_study} succesfully saved")

    # Catch the Integrity exception
    except IntegrityError:
        db.session.rollback()
        return make_response(f"metadata of {new_study} already exists")



# Show data to user
@app.route('/view', methods = ['GET'])
def fetch_data():
    # join database tables and store it in results variable
    results = db.session.query(Study, Sample, Experiment, File).select_from(Study).join(Sample).join(Experiment).join(File).all()

    # Check if db returns any results
    if len(results) == 0:
        return make_response("The database is empty. Propage it with import_data.py")

    return render_template('table.html', results=results)

