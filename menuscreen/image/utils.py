import os
import secrets
from PIL import Image
from flask import current_app
from flask_login import current_user

from menuscreen import db
from menuscreen.models import (Image_list_history)

def _getImages(id):
    images = db.session.query(
        Image_list_history.id,
        Image_list_history.logo_image_name,
        Image_list_history.logo_image_file,
        Image_list_history.venue_db_id,
    ).filter(Image_list_history.venue_db_id == id
    ).all()
    # for i in images:
    #     print(i.logo_image_file)
        # with open(i.logo_image_file, 'rb') as img:
        #     image=img.read()
        #     print(image)

    imgs = []
    for image in images:
        img = {
            "id": image.id,
            "logo_image_name": image.logo_image_name,
            "logo_image_file": image.logo_image_file,
            "venue_db_id": image.venue_db_id
        }
        imgs.append(img)
    return imgs

def save_image(form_image):
    random_hex = secrets.token_hex(8)
    print(random_hex)
    _, f_ext = os.path.splitext(form_image.filename)
    picture_fn = random_hex + f_ext
    print(picture_fn)
    picture_path = os.path.join(current_app.root_path, 'static/img/logo_images', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
