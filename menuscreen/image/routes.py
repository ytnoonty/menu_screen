from flask import (render_template, url_for, flash, redirect,
                    Blueprint, current_app)
from flask_login import (login_user, current_user, login_required)
from menuscreen import db
from menuscreen.models import (Image_list_history)
from menuscreen.image.forms import (ImageForm)
from menuscreen.image.utils import (_getImages, save_icon_image, save_full_image)


image = Blueprint('image', __name__)


# add image to DB
@image.route('/add_image', methods=['GET','POST'])
@login_required
def add_image():
    form = ImageForm()
    # validate and submit the form
    if form.validate_on_submit():
        imgName = form.imageName.data
        imgFile = form.imageFile.data
        print(imgName)
        print(imgFile)

        # if form fields are populated save image file to server
        if form.imageFile.data:
            # save image icon 125px x 125px
            img_icon_file = save_icon_image(form.imageFile.data)
            # save image normal size
            img_file = save_full_image(form.imageFile.data)

        # send image icon info to DB
        imgIcon = Image_list_history(
            logo_image_name=imgName + "_icon",
            logo_image_file=img_icon_file,
            venue_db_id=current_user.id
        )
        db.session.add(imgIcon)
        # db.session.commit()

        # send image normal size info to DB
        img = Image_list_history(
            logo_image_name=imgName + "_full",
            logo_image_file=img_file,
            venue_db_id=current_user.id
        )
        db.session.add(img)
        db.session.commit()

        # show success message
        flash('Image has been added to the list!', 'success')
        return redirect(url_for('image.image_dashboard'))
    return render_template('add_image.html', title='Add Image', legend="Add Image", form=form)

# image/logo dashboard
@image.route('/image_dashboard', methods=['GET','POST'])
@login_required
def image_dashboard():
    images = _getImages(current_user.id)
    for image in images:
        print(image['logo_image_name'])
        image['img'] = url_for('static', filename='img/logo_images/' + image['logo_image_file'])

        # if image['logo_image_file']:

            # with open('logo.jpg', 'wb') as l:
            #     l.write(image['logo_image_file'])

        # # image.dash_menu_id = list(image.logo_image_name)[0].lower()

    if images:
        return render_template('image_dashboard.html', title='Image Dashboard', legend='Image Dashboard', images=images)
    else:
        msg = 'Sorry, no images found!'
    return render_template('image_dashboard.html', title='Image Dashboard', legend='Image Dashboard', msg=msg)

# edit_image
@image.route('/edit_image/<string:image_id>', methods=['GET','POST'])
@login_required
def edit_image(image_id):

    # check if form is validated and method == POST
    if form.validate_on_submit():
        # show success message
        flash('Image has been updated!', 'success')
        return redirect(url_for('image.image_dashboard'))
    elif request.method == 'GET':
        print(image_id)
    return render_template('edit_image.html', title='Edit Image: '+ image_id,
    legend='Edit Image'+ image_id)

# delete image
@image.route('/delete_image/<string:image_id>', methods=['POST'])
@login_required
def delete_image(image_id):
    print(image_id)
    flash('The image has been deleted!', 'success')
    return redirect(url_for('image.image_dashboard'))
