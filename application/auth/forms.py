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

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username).first()
    #     # email = User.query.filter_by(email=email).first()
    #     if user:
    #         print('!!!')
    #         raise ValidationError('Username already exits')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[ InputRequired() ])
    password = PasswordField('Password', validators=[ InputRequired()] )
    submit = SubmitField('Submit')
