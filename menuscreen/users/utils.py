import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from menuscreen import mail

from menuscreen import db
from menuscreen.models import User, List_history, List_current

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/img/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# function to send user an email with link and a tokey to to allow the user to reset their password
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                    sender='noreply@demo.com',
                    recipients=[user.email])
    msg.body = '''To reset your password, visit the following link: {}
If you did not make this request then simply ignore this email and no changes will be made.
'''.format(url_for('users.reset_token', token=token, _external=True))
    mail.send(msg)


def get_user_data(user_id):
    user = User.query.filter_by(id=user_id).first()
    data = {}
    data['id'] = user.id,
    data['venue_name'] = user.venue_name,
    # data['name'] = user.name,
    # data['email'] = user.email,
    # data['username'] = user.username,
    # data['password'] = user.password,
    # data['image_file'] = user.image_file
    return data
