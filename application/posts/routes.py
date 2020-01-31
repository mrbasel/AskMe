from flask import Blueprint, request, url_for, render_template, redirect, flash
from flask_login import current_user
from application.models import Question, Answer
from application import db

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static', static_url_path='/posts/static')


@posts.route('/ask-question', methods=['GET', 'POST'])
def askQuestion():
    if request.form:
        if current_user.is_anonymous:
            flash('You have to login to post questions', 'info')
            return redirect(url_for('main.home'))
        else:

            userQuestion = request.form.get('question')
            questionTag = request.form.get('tags')
            question = Question(content=userQuestion, tags=questionTag, askerId=current_user.id)

            db.session.add(question)
            db.session.commit()
            return redirect(url_for('main.home'))


# This route contains the answers for provided question
@posts.route('/question/<int:questionId>/answers', methods=['GET', 'POST'])
def answersPage(questionId):
    question = Question.query.get(questionId)
    answers = Answer.query.filter_by(questionId=question.id).all()
    return render_template('answers.html', question=question, answers=answers)



# This route is for answering a specfic question
@posts.route('/question/<int:questionId>/answer', methods=['GET', 'POST'])
def answerPage(questionId):
    question = Question.query.get(questionId)

    if current_user.is_anonymous:
        flash('You need to login to answer questions', 'info')
        return redirect(url_for('auth.loginPage'))

    if request.form:
        answerContent = request.form.get('answer')
        answer = Answer(answerContent=answerContent, questionId=questionId, answerer=current_user)

        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('answer.html', question=question)
