import os

class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('askme_db_uri')
    SQLALCHEMY_DATABASE_URI = 'postgres://leuzjgbwfdylyq:0515b7c87ce701cee2a11a445b4609685c8d48d84427d86a5a5f5a260b841367@ec2-35-175-170-131.compute-1.amazonaws.com:5432/d3stpbfkacs5he'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('askme_secret_key')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    ALLOWED_EXTENTIONS = ['png', 'svg']
