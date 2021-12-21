from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


# Set up database - metadata.db will be the file it will look for
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metadata.db'

# Initialize db
db = SQLAlchemy(app)

from flask_app import routes