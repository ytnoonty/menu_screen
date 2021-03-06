from flask import render_template, request, Response, Blueprint
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import User, List_history, List_current


main = Blueprint('main', __name__)

@main.route('/')
def index():
    # return render_template('index.html', title='Index', current_user=current_user)
    return render_template('home.html', title='Index', current_user=current_user)

@main.route('/home')
def home():
    return render_template('home.html', title='Home', current_user=current_user)
