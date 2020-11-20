from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required

from ..models import User
from .forms import LoginForm
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
   logout_user() 
   flash('You have been logged out.')
   return redirect(url_for('main.inedx'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)
