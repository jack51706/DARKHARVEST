import os

# basedir definied to create directory if necessary
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-wirl-nerver-guerss'

    # Defines database configuration information
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Tell bootstrap to pull from localhost
    # BOOTSTRAP_SERVE_LOCAL = True