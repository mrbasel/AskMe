from flask import Blueprint, render_template
from application.models import Question


main = Blueprint('main', __name__, template_folder='templates')




@main.route('/')
@main.route('/home')
def home():
    questions = Question.query.all()
    return render_template('main.html', questions=questions)
