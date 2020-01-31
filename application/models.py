from flask_sqlalchemy import SQLAlchemy
from application import db, loginManager
from flask_login import UserMixin


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), unique=False, nullable=False)
    tags = db.Column(db.String(20), nullable=True, unique=False)
    answers = db.relationship('Answer', backref='question')
    askerId = db.Column(db.Integer, db.ForeignKey('user.id'))
    # likes = db.Column(db.Integer)
    def __repr__(self):
        return '<Question ID: {}>'.format(self.id)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answerContent = db.Column(db.String(300), nullable=False, unique=False)
    questionId = db.Column(db.Integer, db.ForeignKey('question.id'))
    answerers = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Answer ID: {}>'.format(self.id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=False)
    questions = db.relationship('Question', backref='asker')
    answers = db.relationship('Answer', backref='answerer')
    profileImg = db.Column(db.String(200), nullable=False, unique=False)
