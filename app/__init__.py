# Flask object is declared and instantiated for further usage.
from flask import Flask

# Config class is made accesible
from config import Config

# Import database framework
from flask_sqlalchemy import SQLAlchemy

# Import database migration framework
from flask_migrate import Migrate

# Import login initialization
from flask_login import LoginManager

# Import BootStrap
from flask_bootstrap import Bootstrap

# Setup rotating log storage
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)

app.config.from_object(Config)


# Initialize database
db = SQLAlchemy(app)

# Initialize database migration
migrate = Migrate(app, db)

# Initialize login 
login = LoginManager(app)
login.login_view = 'login'

# Initialize Bootstrap
bootstrap = Bootstrap(app)



# Makes accessible .py files in the app directory
from app import routes, models, errors

if not app.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/DARKHARVEST.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('DARKHARVEST startup')