# Metadata registry

This is an application to read the metadata from a JSON file, populate the database with metadata and display it. Please note that the JSON file should follow the same schema as the example file given [here](https://github.com/sbilge/GHGA_APP/blob/main/test_data/metadata.json). The application assumes there should be one JSON file per study. If you have two JSON file belongs to same Study, merge them before importing data to database.

## Getting started

1. Clone GitHub repository  
`git clone https://github.com/sbilge/GHGA_APP.git`

2. change directory into cloned folder  
`cd GHGA_APP`

3. Create conda environment from `environment.yml`  
`conda env create -f environment.yml`

4. Activate environment  
`conda activate ghga_app`

5. Start the flask app  
`python run.py`

6. To upload metadata, open a new terminal with ghga_app as conda environment and change the directory into GHGA_APP via   
`cd GHGA_APP`  
Then import the data via  
`python import_data.py -f <JSON_FILE>`  
To import data from example database run  
`python import_data.py -f test_data/metadata.json`

7. View metadata on `http://localhost:5000/view`

