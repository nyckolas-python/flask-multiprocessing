from app import app
from flask import (render_template, request, redirect, \
                    url_for, flash, jsonify)
from flask_login import login_required, login_user, logout_user

from models import User, Announcements, add_announcements
from forms import LoginForm
from utils import get_items


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('olx'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))


@app.route('/olx')
@login_required
def olx():
    if request.is_json:
        if request.method == 'GET':
            items = get_items()
            add_announcements(items[:5])
            # в самом парсере проверяем айди перед парсингом, после парсим и отдаём
            return jsonify(items[:5])
    return render_template('olx.html')