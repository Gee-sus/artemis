from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Use SQLite locally, MySQL on PythonAnywhere
if 'PYTHONANYWHERE_SITE' in os.environ:
    # PythonAnywhere MySQL configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://geesus:arsenal771992@geesus.mysql.pythonanywhere-services.com/geesus$default'
else:
    # Local SQLite configuration
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models 