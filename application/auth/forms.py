from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, InputRequired, EqualTo, ValidationError
from application.models import User

class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=15), InputRequired() ])
    email =  StringField('Email', validators=[Length(min=6, max=40), InputRequired()])
    password = PasswordField('Password', validators=[EqualTo('confirmPassword'), InputRequired()])
    confirmPassword = PasswordField('ConfirmPassword', validators=[InputRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[ InputRequired() ])
    password = PasswordField('Password', validators=[ InputRequired()] )
    submit = SubmitField('Submit')
