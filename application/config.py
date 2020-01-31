import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('askme_db_uri')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('askme_secret_key')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
