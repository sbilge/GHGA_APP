from flask_app import db


class Study(db.Model):
    __tablename__ = 'study'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    description = db.Column(db.String(200))
    samples = db.relationship('Sample', backref='study', lazy=True)

    def __repr__(self): 
        return f"Study('{self.name}', '{self.description}')"


class Sample(db.Model):
    __tablename__ = 'sample'
    id = db.Column(db.Integer, primary_key = True)
    donor_age = db.Column(db.Integer, nullable = False)
    donor_sex = db.Column(db.String(10), nullable = False)
    tissue_type = db.Column(db.String(50), nullable = False)
    study_id = db.Column(db.Integer, db.ForeignKey('study.id'), nullable = False)
    experiments = db.relationship('Experiment', backref = 'sample', lazy=True)

    def __repr__(self): 
        return f"Study('{self.donor_age}', '{self.donor_sex}','{self.tissue_type}')"


class Experiment(db.Model):
    __tablename__ = 'experiment'
    id = db.Column(db.Integer, primary_key = True)
    experiment_type = db.Column(db.String(10), nullable = False)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'), nullable = False)
    files = db.relationship('File', backref = 'experiment', lazy=True)

    def __repr__(self):
        return f"Experiment('{self.experiment_type}')"


class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key = True)
    file_name = db.Column(db.String(100), nullable = False)
    file_size = db.Column(db.Integer, nullable = False)
    checksum = db.Column(db.String(100), nullable = False)
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id'), nullable = False)

    def __repr__(self):
        return f"File('{self.file_name}', '{self.file_size}', '{self.checksum}')"