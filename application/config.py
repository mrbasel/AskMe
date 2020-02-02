import os

project_dir = os.path.dirname(os.path.abspath(__file__))

class Config:
    db_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') # Set your SECRET KEY here
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') # Set the url to the folder you want to upload images to
    ALLOWED_EXTENTIONS = ['png', 'svg']
