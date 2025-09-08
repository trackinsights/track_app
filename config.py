import os

class Config:
    # Flask settings
    DEBUG = True                  # turn off in production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_secret_key'

    # SQLAlchemy / SQLite settings
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'Track.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
