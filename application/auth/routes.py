from flask import Blueprint, request, url_for, render_template, redirect, flash
from application.models import User
from flask_login import login_user, current_user, logout_user, login_required
from application import bcrypt
from application.auth.forms import RegisterationForm, LoginForm
from application import db

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='/auth/static')


@auth.route('/register', methods=['GET', 'POST'])
def registerationPage():
    form = RegisterationForm(request.form)
    if current_user.is_authenticated:
        flash("Your already logged in", 'info')
        return redirect(url_for('main.home'))

    if request.form and form.validate() == False:
        for field_name, field_errors in form.errors.items():
            for error in field_errors:
                flash(f'{field_name}: {error}')
        return redirect(url_for('auth.registerationPage'))

    elif form.validate_on_submit():
        info = {
        'username': form.username.data,
        'email': form.email.data,
        'password': bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        }
        user = User(username=info['username'], email=info['email'], password=info['password'], profileImg='/static/icons/user-profile-img.svg')

        try:
            db.session.add(user)
            db.session.commit()
            flash('Successfuly registered', 'success')
            return redirect(url_for('main.home'))

        except IntegrityError as e:
            dbErrorMsg = 'Username or Email already used'
            flash(dbErrorMsg, 'formError')
            return redirect(url_for('auth.registerationPage'))

    return render_template('register.html', form=form)


@auth.route('/login', methods=['POST', 'GET'])
def loginPage():
    form = LoginForm()

    if current_user.is_authenticated:
        flash("Your already logged in", 'info')
        return redirect(url_for('main.home'))

    if request.form:
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash('Login successful', 'success')
            login_user(user)
            return redirect(url_for('main.home'))

        else:
            flash('Username or password incorrect', 'formError')
            return redirect(url_for('auth.loginPage'))

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
