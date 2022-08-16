from flask import Blueprint
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

parser = Blueprint('parser', __name__, template_folder='templates')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=6, max=25)], render_kw={'placeholder': 'Username'})
    password = StringField(validators=[InputRequired(), Length(min=6, max=25)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Submit')


@parser.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('olx_app/login.html', form=form)