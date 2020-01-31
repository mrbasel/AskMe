from flask import Blueprint, request, url_for, render_template, redirect, flash, current_app
from flask_login import current_user
from application import db
from application.models import Question, Answer
from werkzeug.utils import secure_filename
import os

profile = Blueprint('profile', __name__, template_folder='templates', static_folder='static', static_url_path='/profile/static')


@profile.route('/profile')
def profilePage():
    if current_user.is_anonymous:
        flash('You need to login to view your profile.', 'info')
        return redirect(url_for('main.home'))

    questions = Question.query.filter_by(askerId=current_user.id).all()
    answers = current_user.answers
    return render_template('profile.html', questions=questions, answers=answers)


@profile.route('/profile/question/<int:questionId>/delete', methods=['GET', 'POST'])
def deleteQuestion(questionId):
    question = Question.query.get(questionId)
    answers = Answer.query.filter_by(questionId=questionId).all()

    [db.session.delete(answer) for answer in answers]
    db.session.delete(question)
    db.session.commit()
    flash(f"question {questionId} and it's answers have been deleted", 'info')
    return redirect(url_for('profile.profilePage'))


@profile.route('/profile/answer/<string:answerId>/delete', methods=['GET', 'POST'])
def deleteAnswer(answerId):
    answer = Answer.query.get(answerId)
    db.session.delete(answer)
    db.session.commit()
    print(f"Answer {answerId} Deleted.", 'info')
    return redirect(url_for('profile.profilePage'))


def is_allowed(filename):
    return True if filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENTIONS'] else False

@profile.route('/profile/edit-photo', methods=['POST', 'GET'])
def editPhoto():
     if request.method == 'POST':
         if request.files:
             image = request.files['image']
             if image:
                 if is_allowed(image.filename):
                     imgFile = secure_filename(image.filename)
                     image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], imgFile))

                     current_user.profileImg = f'/static/photos/{imgFile}'
                     db.session.commit()
                 else:
                     flash('Extention not allowed', 'error')
             else:
                 flash('No image found', 'info')

     return redirect(url_for('profile.profilePage'))
