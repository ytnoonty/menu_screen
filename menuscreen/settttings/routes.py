from flask import (render_template, url_for, flash, redirect,
                    request, abort, jsonify, Blueprint)
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import User, Beerscreen_setting, Winecreen_setting, Eventscreen_setting, Itemscreen_setting, Font_size_option, Template, Drink_size, Drink_price
from menuscreen.settttings.forms import BeerscreenSettingsForm, WinecreenSettingsForm, EventscreenSettingsForm, ItemscreenSettingsForm, FontSizeForm, TemplateForm, DrinkContainerSizeForm, DrinkPriceForm, ImageForm
from menuscreen.settttings.utils import _getFontSizes, _getFontSizeOptions, _getTemplates, _getBeerSettings, _getNameFontSize, _getStyleFontSize, _getTemplateName, _getAbvFontSize, _getIbuFontSize, _getBreweryFontSize, _getDrinkSizes, _getDrinkPrices, _getImages
from menuscreen.list_history.utils import _getCurrentBeerlist
from menuscreen.event.utils import _getEventsSortAsc
from menuscreen.users.init_db_tables import getVenueId

from menuscreen import pusher_client

settttings = Blueprint('settttings', __name__)

# GET USER SETTINGS
@settttings.route('/_get_beerscreen_settings', methods=['GET', 'POST'])
# @login_required
def _get_beerscreen_settings():
    data = request.get_json()
    print("**************************************")
    print("******LINE  22***********************")
    print("settttings. /_get_beerscreen_settings")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")

    if (current_user.is_authenticated):
        print("LOGGED IN")
        print(current_user.id)

        data['userId'] = current_user.id
        print("data: {}".format(data))
        data = _getBeerSettings(data)
    elif (data):
        print("NOT LOGGED IN")
        print(data['userName'])
        current_user_id = getVenueId(data['userName'])
        print(current_user_id)
        data['userId'] = current_user_id
        print("data: {}".format(data))
        data = _getBeerSettings(data)
    else:
        print("NOT LOGGED IN AND NO URL INFO")
        data = {}
    print("**************************************")
    print("**************************************")
    return jsonify(data)

# GET FONTSIZEOPTIONS
@settttings.route('/_get_font_size_options', methods=['POST'])
@login_required
def get_font_size_options():
    data = request.get_json()
    print("**************************************")
    print("******LINE  57***********************")
    print("settttings. /_get_font_size_options")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")

    if (current_user.is_authenticated):
        print("LOGGED IN")
        print(current_user.id)

        data['userId'] = current_user.id
        print("data: {}".format(data))
        data = _getFontSizeOptions(data['userId'])
    elif (data):
        print("NOT LOGGED IN")
        print(data['userName'])
        current_user_id = getVenueId(data['userName'])
        print(current_user_id)
        data['userId'] = current_user_id
        print("data: {}".format(data))
        data = _getFontSizeOptions(data['userId'])
    else:
        print("NOT LOGGED IN AND NO URL INFO")
        data = {}
    print("**************************************")
    print("**************************************")
    return jsonify(data)


# Add template to DB
@settttings.route('/add_template', methods=['GET', 'POST'])
@login_required
def add_template():
    form = TemplateForm(request.form)
    templates = _getTemplates(current_user.id)
    form.templateSelect.choices = [(template['id'], template['template_name']) for template in templates]

    if form.validate_on_submit():
        templateName = request.form['templateName']
        newTemplate = Template(template_name=templateName, screen_number=1, active_template='disabled', venue_db_id=current_user.id)
        db.session.add(newTemplate)
        db.session.commit()
        flash('New Template has been added!', 'success')
        return redirect( url_for('settttings.add_template'))
    return render_template('add_template.html', title='Add Templates', legend='Edit Templates', form=form)

# Add font size to DB
@settttings.route('/add_font_size', methods=['GET','POST'])
@login_required
def add_font_size():
    form = FontSizeForm(request.form)
    sizes = _getFontSizes(current_user.id)
    form.fontSizes.choices = [(size['id'], size['font_sizes']) for size in sizes]

    if form.validate_on_submit():
        fontSize = request.form['fontSizeOptions'] + 'em'
        newFontSize = Font_size_option(font_sizes=fontSize, venue_db_id=current_user.id)
        db.session.add(newFontSize)
        db.session.commit()
        flash('New Font size has been added!', 'success')
        return redirect(url_for('settttings.add_font_size'))
    return render_template('add_font_size.html', title='Edit Font Sizes', legend='Edit Font Size List', form=form)

# Edit drink container size
@settttings.route('/edit_drink_size', methods=['GET','POST'])
@login_required
def edit_drink_size():
    form = DrinkContainerSizeForm(request.form)
    sizes = _getDrinkSizes(current_user.id)

    form.drinkSizeSelect.choices = [(size['id'], size['drink_size']) for size in sizes]

    if form.validate_on_submit():
        drinkSize = request.form['drinkSizeText']
        newDrinkSize = Drink_size(drink_size=drinkSize, venue_db_id=current_user.id)
        db.session.add(newDrinkSize)
        db.session.commit()
        flash('New Drink size has been added!', 'success')
        return redirect(url_for('settttings.edit_drink_size'))
    return render_template('edit_drink_size.html', title='Edit Drink Sizes', legend='Edit Drink Sizes', form=form)

# Edit drink price
@settttings.route('/edit_drink_price', methods=['GET','POST'])
@login_required
def edit_drink_price():
    form = DrinkPriceForm(request.form)
    prices = _getDrinkPrices(current_user.id)

    form.drinkPriceSelect.choices = [(price['id'], price['drink_price']) for price in prices]

    if form.validate_on_submit():
        drinkPrice = request.form['drinkPriceText']
        newDrinkPrice = Drink_price(drink_price=drinkPrice, venue_db_id=current_user.id)
        db.session.add(newDrinkPrice)
        db.session.commit()
        flash('New Drink price has been added!', 'success')
        return redirect(url_for('settttings.edit_drink_price'))
    return render_template('edit_drink_price.html', title='Edit Drink Prices', legend='Edit Drink Prices', form=form)


# add image to DB
@settttings.route('/add_image', methods=['GET','POST'])
@login_required
def add_image():
    form = ImageForm()
    # validate and submit the form
    if form.validate_on_submit():
        print(form.imageName.data)
        print(form.imageFile.data)
        #show success message
        flash('Image has been added to the list!', 'success')
        return redirect(url_for('settttings.image_dashboard'))
    return render_template('add_image.html', title='Add Image', legend="Add Image", form=form)

# image/logo dashboard
@settttings.route('/image_dashboard', methods=['GET','POST'])
@login_required
def image_dashboard():
    images = _getImages(current_user.id)
    for image in images:
        print(image)
        # image.dash_menu_id = list(image.logo_image_name)[0].lower()
    if images:
        return render_template('image_dashboard.html', title='Image Dashboard', legend='Image Dashboard', images=images)
    else:
        msg = 'Sorry, no images found!'
    return render_template('image_dashboard.html', title='Image Dashboard', legend='Image Dashboard', msg=msg)

# edit_image
@settttings.route('/edit_image/<string:image_id>', methods=['GET','POST'])
@login_required
def edit_image(image_id):

    # check if form is validated and method == POST
    if form.validate_on_submit():
        # show success message
        flash('Image has been updated!', 'success')
        return redirect(url_for('settttings.image_dashboard'))
    elif request.method == 'GET':
        print(image_id)
    return render_template('edit_image.html', title='Edit Image: '+ image_id,
    legend='Edit Image'+ image_id)

# delete image
@settttings.route('/delete_image/<string:image_id>', methods=['POST'])
@login_required
def delete_image(image_id):
    print(image_id)
    flash('The image has been deleted!', 'success')
    return redirect(url_for('settttings.image_dashboard'))





# beerscreen_settings page
@settttings.route('/beerscreen_settings', methods=['GET', 'POST'])
@login_required
def beerscreen_settings():
    print("``````````````````````````````````````````````````````````````````")
    print("``````````````````````````````````````````````````````````````````")
    print("`````````````````````BEERSCREEN_SETTINGS``````````````````````````")
    print("``````````````````````````````````````````````````````````````````")
    print("``````````````````````````````````````````````````````````````````")

    print("``````````````````````````````````````````````````````````````````")
    print("``````````````````````````````````````````````````````````````````")
    print("``````````````````````````FROM HERE NOW```````````````````````````")
    form = BeerscreenSettingsForm(request.form)
    # print(form.__dict__)
    # print(form['fontColorThree'])
    # print(form['beerSettingsScreenId'])
    # for attr, value in form.__dict__.iteritems():
    #     print(attr, value)

    print("``````````````````````````````````````````````````````````````````")
    print("``````````````````````````````````````````````````````````````````")

    screenId = 1
    screenData = {
        "userId": current_user.id,
        "screenNumber": screenId,
    }

    settings = _getBeerSettings(screenData)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(settings)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


    form = BeerscreenSettingsForm(request.form,
        fontColorOne = settings['fontColorOne'],
        fontColorTwo = settings['fontColorTwo'],
        fontColorThree = settings['fontColorThree'],
        fontColorDirection = settings['fontColorDirection'],
        shadowFontColorOne = settings['shadowFontColorOne'],
        shadowFontColorTwo = settings['shadowFontColorTwo'],
        shadowFontColorThree = settings['shadowFontColorThree'],
        shadowFontColorDirection = settings['shadowFontColorDirection'],

        screenTemplate = settings['screenTemplate'],
        beerscreenLandscapePortraitToggle = settings['beerscreenLandscapePortraitToggle'],

        beerBomBgColorOne = settings['beerBomBgColorOne'],
        beerBomBgColorTwo = settings['beerBomBgColorTwo'],
        beerBomBgColorThree = settings['beerBomBgColorThree'],
        beerBomBgColorFour = settings['beerBomBgColorFour'],
        beerBomBgColorFive = settings['beerBomBgColorFive'],
        beerBomBgColorDirection = settings['beerBomBgColorDirection'],

        beerBomNameFont = settings['beerBomNameFont'],
        beerBomNameFontColor = settings['beerBomNameFontColor'],
        beerBomNameFontSize = settings['beerBomNameFontSize'],
        beerBomNameFontBoldToggle = settings['beerBomNameFontBoldToggle'],
        beerBomNameFontItalicToggle = settings['beerBomNameFontItalicToggle'],
        beerBomNameFontUnderlineToggle = settings['beerBomNameFontUnderlineToggle'],

        beerBomStyleFont = settings['beerBomStyleFont'],
        beerBomStyleFontColor = settings['beerBomStyleFontColor'],
        beerBomStyleFontSize = settings['beerBomStyleFontSize'],
        beerBomStyleFontBoldToggle = settings['beerBomStyleFontBoldToggle'],
        beerBomStyleFontItalicToggle = settings['beerBomStyleFontItalicToggle'],
        beerBomStyleFontUnderlineToggle = settings['beerBomStyleFontUnderlineToggle'],

        beerBomAbvFontColor = settings['beerBomAbvFontColor'],
        beerBomAbvFontSize = settings['beerBomAbvFontSize'],
        beerBomAbvFontBoldToggle = settings['beerBomAbvFontBoldToggle'],
        beerBomAbvFontItalicToggle = settings['beerBomAbvFontItalicToggle'],
        beerBomAbvFontUnderlineToggle = settings['beerBomAbvFontUnderlineToggle'],

        beerBomIbuFontColor = settings['beerBomIbuFontColor'],
        beerBomIbuFontSize = settings['beerBomIbuFontSize'],
        beerBomIbuFontBoldToggle = settings['beerBomIbuFontBoldToggle'],
        beerBomIbuFontItalicToggle = settings['beerBomIbuFontItalicToggle'],
        beerBomIbuFontUnderlineToggle = settings['beerBomIbuFontUnderlineToggle'],

        beerBomBreweryFont = settings['beerBomBreweryFont'],
        beerBomBreweryFontColor = settings['beerBomBreweryFontColor'],
        beerBomBreweryFontSize = settings['beerBomBreweryFontSize'],
        beerBomBreweryFontBoldToggle = settings['beerBomBreweryFontBoldToggle'],
        beerBomBreweryFontItalicToggle = settings['beerBomBreweryFontItalicToggle'],
        beerBomBreweryFontUnderlineToggle = settings['beerBomBreweryFontUnderlineToggle'],

        beerBgColorOne = settings['beerBgColorOne'],
        beerBgColorTwo = settings['beerBgColorTwo'],
        beerBgColorThree = settings['beerBgColorThree'],
        beerBgColorFour = settings['beerBgColorFour'],
        beerBgColorFive = settings['beerBgColorFive'],
        beerBgColorDirection = settings['beerBgColorDirection'],

        beerNameFont = settings['beerNameFont'],
        beerNameFontColor = settings['beerNameFontColor'],
        beerNameFontSize = settings['beerNameFontSize'],
        beerNameFontBoldToggle = settings['beerNameFontBoldToggle'],
        beerNameFontItalicToggle = settings['beerNameFontItalicToggle'],
        beerNameFontUnderlineToggle = settings['beerNameFontUnderlineToggle'],

        beerStyleFont = settings['beerStyleFont'],
        beerStyleFontColor = settings['beerStyleFontColor'],
        beerStyleFontSize = settings['beerStyleFontSize'],
        beerStyleFontBoldToggle = settings['beerStyleFontBoldToggle'],
        beerStyleFontItalicToggle = settings['beerStyleFontItalicToggle'],
        beerStyleFontUnderlineToggle = settings['beerStyleFontUnderlineToggle'],

        beerAbvFontColor = settings['beerAbvFontColor'],
        beerAbvFontSize = settings['beerAbvFontSize'],
        beerAbvFontBoldToggle = settings['beerAbvFontBoldToggle'],
        beerAbvFontItalicToggle = settings['beerAbvFontItalicToggle'],
        beerAbvFontUnderlineToggle = settings['beerAbvFontUnderlineToggle'],

        beerIbuFontColor = settings['beerIbuFontColor'],
        beerIbuFontSize = settings['beerIbuFontSize'],
        beerIbuFontBoldToggle = settings['beerIbuFontBoldToggle'],
        beerIbuFontItalicToggle = settings['beerIbuFontItalicToggle'],
        beerIbuFontUnderlineToggle = settings['beerIbuFontUnderlineToggle'],

        beerBreweryFont = settings['beerBreweryFont'],
        beerBreweryFontColor = settings['beerBreweryFontColor'],
        beerBreweryFontSize = settings['beerBreweryFontSize'],
        beerBreweryFontBoldToggle = settings['beerBreweryFontBoldToggle'],
        beerBreweryFontItalicToggle = settings['beerBreweryFontItalicToggle'],
        beerBreweryFontUnderlineToggle = settings['beerBreweryFontUnderlineToggle'],

        beerTickerBgColorOne = settings['beerTickerBgColorOne'],
        beerTickerBgColorTwo = settings['beerTickerBgColorTwo'],
        beerTickerBgColorThree = settings['beerTickerBgColorThree'],
        beerTickerBgColorFour = settings['beerTickerBgColorFour'],
        beerTickerBgColorFive = settings['beerTickerBgColorFive'],
        beerTickerBgColorDirection = settings['beerTickerBgColorDirection'],

        beerTickerBeernamesFont = settings['beerTickerBeernamesFont'],
        beerTickerFont = settings['beerTickerFont'],
        beerTickerFontColor = settings['beerTickerFontColor'],
        beerTickerFontSize = settings['beerTickerFontSize'],
        beerTickerFontBoldToggle = settings['beerTickerFontBoldToggle'],
        beerTickerFontItalicToggle = settings['beerTickerFontItalicToggle'],
        beerTickerFontUnderlineToggle = settings['beerTickerFontUnderlineToggle'],

        beerTickerToggle = settings['beerTickerToggle'],
        beerTickerScrollSpeed = settings['beerTickerScrollSpeed'],

        beerSettingsScreenId = settings['beerSettingsScreenId'],
        beerscreenTemplate = settings['beerscreenTemplate'],
        venueDbId = settings['venueDbId'],
        templateName = settings['templateName'],
    )

    beerscreenSettings = db.session.query(
    Beerscreen_setting.beer_settings_screen_id
    ).filter(Beerscreen_setting.venue_db_id == current_user.id
    ).all()
    beerscreenSettingsIds = []
    for id in beerscreenSettings:
        beerscreenSettingsIds.append(id[0])
    # print("beerscreenSettingsIds: {}".format(beerscreenSettingsIds))

    numOfScreens = []
    for x in range(1, len(beerscreenSettingsIds) + 1, 1):
        number = {
            "id":x,
            "number":x,
        }
        numOfScreens.append(number)
    screenNumSettings = numOfScreens
    # print("screenNumSettings: {}".format(screenNumSettings))

    directions = [
        {
            "id":"to bottom",
            "direction":"to bottom",
        },
        {
            "id":"to top",
            "direction":"to top",
        },
        {
            "id":"to left",
            "direction":"to left",
        },
        {
            "id":"to right",
            "direction":"to right",
        },
        {
            "id":"to bottom left",
            "direction":"to bottom left",
        },
        {
            "id":"to bottom right",
            "direction":"to bottom right",
        },
        {
            "id":"to top left",
            "direction":"to top left",
        },
        {
            "id":"to top right",
            "direction":"to top right",
        },
    ]
    fonts = [
        {
            "id":'1',
            "font" : "Times Roman"
        },
        {
            "id":'2',
            "font" : "Courier New"
        }
    ]

    # function called from this module to query font size table
    sizes = _getFontSizes(current_user.id)
    # print(sizes)
    # function called from this module to query template table
    templates = _getTemplates(current_user.id)
    # print(templates)

    form.beerSettingsScreenId.choices = [ (number['id'], number['number']) for number in screenNumSettings ]

    form.fontColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.shadowFontColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.beerBomBgColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.beerBgColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.beerTickerBgColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]

    form.beerNameFont.choices = [ (font['id'], font['font']) for font in fonts ]
    form.beerBomNameFont.choices = [ (font['id'], font['font']) for font in fonts ]
    form.beerBomStyleFont.choices = [ (font['id'], font['font']) for font in fonts ]
    form.beerStyleFont.choices = [ (font['id'], font['font']) for font in fonts ]
    form.beerBomBreweryFont.choices = [ (font['id'], font['font']) for font in fonts ]
    form.beerBreweryFont.choices = [ (font['id'], font['font']) for font in fonts ]
    form.beerTickerBeernamesFont.choices = [ (font['id'], font['font']) for font in fonts ]
    form.beerTickerFont.choices = [ (font['id'], font['font']) for font in fonts ]

    form.beerBomNameFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerBomStyleFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerBomAbvFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerBomIbuFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerBomBreweryFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerBomIbuFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerNameFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerStyleFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerAbvFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerIbuFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerBreweryFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerTickerFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.beerscreenTemplate.choices = [ (template['id'], template['template_name']) for template in templates ]

    if request.method == 'POST' or form.validate_on_submit():
    # if request.method =='POST':
        print('***************************************************************')
        print('***************************************************************')
        print('SUBMITTING SETTINGS DATA NOW')
        print('***************************************************************')
        print('***************************************************************')
        userSettings = {}
        userSettings['fontColorOne'] = form.fontColorOne.data
        userSettings['fontColorTwo'] = form.fontColorTwo.data
        userSettings['fontColorThree'] = form.fontColorThree.data
        userSettings['fontColorDirection'] = form.fontColorDirection.data
        userSettings['shadowFontColorOne'] = form.shadowFontColorOne.data
        userSettings['shadowFontColorTwo'] = form.shadowFontColorTwo.data
        userSettings['shadowFontColorThree'] = form.shadowFontColorThree.data
        userSettings['shadowFontColorDirection'] = form.shadowFontColorDirection.data

        userSettings['beerBomBgColorOne'] = form.beerBomBgColorOne.data
        userSettings['beerBomBgColorTwo'] = form.beerBomBgColorTwo.data
        userSettings['beerBomBgColorThree'] = form.beerBomBgColorThree.data
        userSettings['beerBomBgColorFour'] = form.beerBomBgColorFour.data
        userSettings['beerBomBgColorFive'] = form.beerBomBgColorFive.data
        userSettings['beerBomBgColorDirection'] = form.beerBomBgColorDirection.data

        userSettings['beerBomNameFont'] = form.beerBomNameFont.data
        userSettings['beerBomNameFontColor'] = form.beerBomNameFontColor.data
        userSettings['beerBomNameFontSize'] = form.beerBomNameFontSize.data
        userSettings['beerBomNameFontBoldToggle'] = form.beerBomNameFontBoldToggle.data
        userSettings['beerBomNameFontItalicToggle'] = form.beerBomNameFontItalicToggle.data
        userSettings['beerBomNameFontUnderlineToggle'] = form.beerBomNameFontUnderlineToggle.data

        userSettings['beerBomStyleFont'] = form.beerBomStyleFont.data
        userSettings['beerBomStyleFontColor'] = form.beerBomStyleFontColor.data
        userSettings['beerBomStyleFontSize'] = form.beerBomStyleFontSize.data
        userSettings['beerBomStyleFontBoldToggle'] = form.beerBomStyleFontBoldToggle.data
        userSettings['beerBomStyleFontItalicToggle'] = form.beerBomStyleFontItalicToggle.data
        userSettings['beerBomStyleFontUnderlineToggle'] = form.beerBomStyleFontUnderlineToggle.data

        userSettings['beerBomAbvFontColor'] = form.beerBomAbvFontColor.data
        userSettings['beerBomAbvFontSize'] = form.beerBomAbvFontSize.data
        userSettings['beerBomAbvFontBoldToggle'] = form.beerBomAbvFontBoldToggle.data
        userSettings['beerBomAbvFontItalicToggle'] = form.beerBomAbvFontItalicToggle.data
        userSettings['beerBomAbvFontUnderlineToggle'] = form.beerBomAbvFontUnderlineToggle.data

        userSettings['beerBomIbuFontColor'] = form.beerBomIbuFontColor.data
        userSettings['beerBomIbuFontSize'] = form.beerBomIbuFontSize.data
        userSettings['beerBomIbuFontBoldToggle'] = form.beerBomIbuFontBoldToggle.data
        userSettings['beerBomIbuFontItalicToggle'] = form.beerBomIbuFontItalicToggle.data
        userSettings['beerBomIbuFontUnderlineToggle'] = form.beerBomIbuFontUnderlineToggle.data

        userSettings['beerBomBreweryFont'] = form.beerBomBreweryFont.data
        userSettings['beerBomBreweryFontColof'] = form.beerBomBreweryFontColor.data
        userSettings['beerBomBreweryFontSize'] = form.beerBomBreweryFontSize.data
        userSettings['beerBomBreweryFontBoldToggle'] = form.beerBomBreweryFontBoldToggle.data
        userSettings['beerBomBreweryFontItalicToggle'] = form.beerBomBreweryFontItalicToggle.data
        userSettings['beerBomBreweryFontUnderlineToggle'] = form.beerBomBreweryFontUnderlineToggle.data

        userSettings['beerBgColorOne'] = form.beerBgColorOne.data
        userSettings['beerBgColorTwo'] = form.beerBgColorTwo.data
        userSettings['beerBgColorThree'] = form.beerBgColorThree.data
        userSettings['beerBgColorFour'] = form.beerBgColorFour.data
        userSettings['beerBgColorFive'] = form.beerBgColorFive.data
        userSettings['beerBgColorDirection'] = form.beerBgColorDirection.data

        userSettings['beerNameFont'] = form.beerNameFont.data
        userSettings['beerNameFontColor'] = form.beerNameFontColor.data
        userSettings['beerNameFontSize'] = form.beerNameFontSize.data
        userSettings['beerNameFontBoldToggle'] = form.beerNameFontBoldToggle.data
        userSettings['beerNameFontItalicToggle'] = form.beerNameFontItalicToggle.data
        userSettings['beerNameFontUnderlineToggle'] = form.beerNameFontUnderlineToggle.data

        userSettings['beerStyleFont'] = form.beerStyleFont.data
        userSettings['beerStyleFontColor'] = form.beerStyleFontColor.data
        userSettings['beerStyleFontSize'] = form.beerStyleFontSize.data
        userSettings['beerStyleFontBoldToggle'] = form.beerStyleFontBoldToggle.data
        userSettings['beerStyleFontItalicToggle'] = form.beerStyleFontItalicToggle.data
        userSettings['beerStyleFontUnderlineToggle'] = form.beerStyleFontUnderlineToggle.data

        userSettings['beerAbvFontColor'] = form.beerAbvFontColor.data
        userSettings['beerAbvFontSize'] = form.beerAbvFontSize.data
        userSettings['beerAbvFontBoldToggle'] = form.beerAbvFontBoldToggle.data
        userSettings['beerAbvFontItalicToggle'] = form.beerAbvFontItalicToggle.data
        userSettings['beerAbvFontUnderlineToggle'] = form.beerAbvFontUnderlineToggle.data

        userSettings['beerIbuFontColor'] = form.beerIbuFontColor.data
        userSettings['beerIbuFontSize'] = form.beerIbuFontSize.data
        userSettings['beerIbuFontBoldToggle'] = form.beerIbuFontBoldToggle.data
        userSettings['beerIbuFontItalicToggle'] = form.beerIbuFontItalicToggle.data
        userSettings['beerIbuFontUnderlineToggle'] = form.beerIbuFontUnderlineToggle.data

        userSettings['beerBreweryFont'] = form.beerBreweryFont.data
        userSettings['beerBreweryFontColor'] = form.beerBreweryFontColor.data
        userSettings['beerBreweryFontSize'] = form.beerBreweryFontSize.data
        userSettings['beerBreweryFontBoldToggle'] = form.beerBreweryFontBoldToggle.data
        userSettings['beerBreweryFontItalicToggle'] = form.beerBreweryFontItalicToggle.data
        userSettings['beerBreweryFontUnderlineToggle'] = form.beerBreweryFontUnderlineToggle.data

        userSettings['beerTickerBgColorOne'] = form.beerTickerBgColorOne.data
        userSettings['beerTickerBgColorTwo'] = form.beerTickerBgColorTwo.data
        userSettings['beerTickerBgColorThree'] = form.beerTickerBgColorThree.data
        userSettings['beerTickerBgColorFour'] = form.beerTickerBgColorFour.data
        userSettings['beerTickerBgColorFive'] = form.beerTickerBgColorFive.data
        userSettings['beerTickerBgColorDirection'] = form.beerTickerBgColorDirection.data

        userSettings['beerTickerBeernamesFont'] = form.beerTickerBeernamesFont.data
        userSettings['beerTickerFont'] = form.beerTickerFont.data
        userSettings['beerTickerFontColor'] = form.beerTickerFontColor.data
        userSettings['beerTickerFontSize'] = form.beerTickerFontSize.data
        userSettings['beerTickerFontBoldToggle'] = form.beerTickerFontBoldToggle.data
        userSettings['beerTickerFontItalicToggle'] = form.beerTickerFontItalicToggle.data
        userSettings['beerTickerFontUnderlineToggle'] = form.beerTickerFontUnderlineToggle.data

        userSettings['beerTickerToggle'] = form.beerTickerToggle.data
        userSettings['beerTickerScrollSpeed'] = form.beerTickerScrollSpeed.data

        userSettings['beerSettingsScreenId'] = form.beerSettingsScreenId.data
        userSettings['beerscreenTemplate'] = form.beerscreenTemplate.data
        userSettings['beerscreenLandscapePortraitToggle'] = form.beerscreenLandscapePortraitToggle.data
        userSettings['venue_db_id'] = current_user.id

        settingsCandidate = Beerscreen_setting.query.filter_by(beer_settings_screen_id=userSettings['beerSettingsScreenId'], venue_db_id=userSettings['venue_db_id']).first()

        settingsCandidate.font_color_one = userSettings['fontColorOne']
        settingsCandidate.font_color_two = userSettings['fontColorTwo']
        settingsCandidate.font_color_three = userSettings['fontColorThree']
        settingsCandidate.font_color_direction = userSettings['fontColorDirection']
        settingsCandidate.shadow_font_color_one = userSettings['shadowFontColorOne']
        settingsCandidate.shadow_font_color_two = userSettings['shadowFontColorTwo']
        settingsCandidate.shadow_font_color_three = userSettings['shadowFontColorThree']
        settingsCandidate.shadow_font_color_direction = userSettings['shadowFontColorDirection']


        settingsCandidate.beer_bom_background_color_one = userSettings['beerBomBgColorOne']
        settingsCandidate.beer_bom_background_color_two = userSettings['beerBomBgColorTwo']
        settingsCandidate.beer_bom_background_color_three = userSettings['beerBomBgColorThree']
        settingsCandidate.beer_bom_background_color_four = userSettings['beerBomBgColorFour']
        settingsCandidate.beer_bom_background_color_five = userSettings['beerBomBgColorFive']
        settingsCandidate.beer_bom_background_color_direction = userSettings['beerBomBgColorDirection']

        settingsCandidate.beer_bom_name_font = userSettings['beerBomNameFont']
        settingsCandidate.beer_bom_name_font_color = userSettings['beerBomNameFontColor']
        settingsCandidate.beer_bom_name_font_size = userSettings['beerBomNameFontSize']
        settingsCandidate.beer_bom_name_font_bold_toggle = userSettings['beerBomNameFontBoldToggle']
        settingsCandidate.beer_bom_name_font_italic_toggle = userSettings['beerBomNameFontItalicToggle']
        settingsCandidate.beer_bom_name_font_underline_toggle = userSettings['beerBomNameFontUnderlineToggle']

        settingsCandidate.beer_bom_style_font = userSettings['beerBomStyleFont']
        settingsCandidate.beer_bom_style_font_color = userSettings['beerBomStyleFontColor']
        settingsCandidate.beer_bom_style_font_size = userSettings['beerBomStyleFontSize']
        settingsCandidate.beer_bom_style_font_bold_toggle = userSettings['beerBomStyleFontBoldToggle']
        settingsCandidate.beer_bom_style_font_italic_toggle = userSettings['beerBomStyleFontItalicToggle']
        settingsCandidate.beer_bom_style_font_underline_toggle = userSettings['beerBomStyleFontUnderlineToggle']

        settingsCandidate.beer_bom_abv_font_color = userSettings['beerBomAbvFontColor']
        settingsCandidate.beer_bom_abv_font_size = userSettings['beerBomAbvFontSize']
        settingsCandidate.beer_bom_abv_font_bold_toggle = userSettings['beerBomAbvFontBoldToggle']
        settingsCandidate.beer_bom_abv_font_italic_toggle = userSettings['beerBomAbvFontItalicToggle']
        settingsCandidate.beer_bom_abv_font_underline_toggle = userSettings['beerBomAbvFontUnderlineToggle']

        settingsCandidate.beer_bom_ibu_font_color = userSettings['beerBomIbuFontColor']
        settingsCandidate.beer_bom_ibu_font_size = userSettings['beerBomIbuFontSize']
        settingsCandidate.beer_bom_ibu_font_bold_toggle = userSettings['beerBomIbuFontBoldToggle']
        settingsCandidate.beer_bom_ibu_font_italic_toggle = userSettings['beerBomIbuFontItalicToggle']
        settingsCandidate.beer_bom_ibu_font_underline_toggle = userSettings['beerBomIbuFontUnderlineToggle']

        settingsCandidate.beer_bom_brewery_font = userSettings['beerBomBreweryFont']
        settingsCandidate.beer_bom_brewery_font_color = userSettings['beerBomBreweryFontColof']
        settingsCandidate.beer_bom_brewery_font_size = userSettings['beerBomBreweryFontSize']
        settingsCandidate.beer_bom_brewery_font_bold_toggle = userSettings['beerBomBreweryFontBoldToggle']
        settingsCandidate.beer_bom_brewery_font_italic_toggle = userSettings['beerBomBreweryFontItalicToggle']
        settingsCandidate.beer_bom_brewery_font_underline_toggle = userSettings['beerBomBreweryFontUnderlineToggle']

        settingsCandidate.beer_background_color_one = userSettings['beerBgColorOne']
        settingsCandidate.beer_background_color_two = userSettings['beerBgColorTwo']
        settingsCandidate.beer_background_color_three = userSettings['beerBgColorThree']
        settingsCandidate.beer_background_color_four = userSettings['beerBgColorFour']
        settingsCandidate.beer_background_color_five = userSettings['beerBgColorFive']
        settingsCandidate.beer_background_color_direction = userSettings['beerBgColorDirection']

        settingsCandidate.beer_name_font = userSettings['beerNameFont']
        settingsCandidate.beer_name_font_color = userSettings['beerNameFontColor']
        settingsCandidate.beer_name_font_size = userSettings['beerNameFontSize']
        settingsCandidate.beer_name_font_bold_toggle = userSettings['beerNameFontBoldToggle']
        settingsCandidate.beer_name_font_italic_toggle = userSettings['beerNameFontItalicToggle']
        settingsCandidate.beer_name_font_underline_toggle = userSettings['beerNameFontUnderlineToggle']

        settingsCandidate.beer_style_font = userSettings['beerStyleFont']
        settingsCandidate.beer_style_font_color = userSettings['beerStyleFontColor']
        settingsCandidate.beer_style_font_size = userSettings['beerStyleFontSize']
        settingsCandidate.beer_style_font_bold_toggle = userSettings['beerStyleFontBoldToggle']
        settingsCandidate.beer_style_font_italic_toggle = userSettings['beerStyleFontItalicToggle']
        settingsCandidate.beer_style_font_underline_toggle = userSettings['beerStyleFontUnderlineToggle']

        settingsCandidate.beer_abv_font_color = userSettings['beerAbvFontColor']
        settingsCandidate.beer_abv_font_size = userSettings['beerAbvFontSize']
        settingsCandidate.beer_abv_font_bold_toggle = userSettings['beerAbvFontBoldToggle']
        settingsCandidate.beer_abv_font_italic_toggle = userSettings['beerAbvFontItalicToggle']
        settingsCandidate.beer_abv_font_underline_toggle = userSettings['beerAbvFontUnderlineToggle']

        settingsCandidate.beer_ibu_font_color = userSettings['beerIbuFontColor']
        settingsCandidate.beer_ibu_font_size = userSettings['beerIbuFontSize']
        settingsCandidate.beer_ibu_font_bold_toggle = userSettings['beerIbuFontBoldToggle']
        settingsCandidate.beer_ibu_font_italic_toggle = userSettings['beerIbuFontItalicToggle']
        settingsCandidate.beer_ibu_font_underline_toggle = userSettings['beerIbuFontUnderlineToggle']

        settingsCandidate.beer_brewery_font = userSettings['beerBreweryFont']
        settingsCandidate.beer_brewery_font_color = userSettings['beerBreweryFontColor']
        settingsCandidate.beer_brewery_font_size = userSettings['beerBreweryFontSize']
        settingsCandidate.beer_brewery_font_bold_toggle = userSettings['beerBreweryFontBoldToggle']
        settingsCandidate.beer_brewery_font_italic_toggle = userSettings['beerBreweryFontItalicToggle']
        settingsCandidate.beer_brewery_font_underline_toggle = userSettings['beerBreweryFontUnderlineToggle']

        settingsCandidate.beer_ticker_bg_color_one = userSettings['beerTickerBgColorOne']
        settingsCandidate.beer_ticker_bg_color_two = userSettings['beerTickerBgColorTwo']
        settingsCandidate.beer_ticker_bg_color_three = userSettings['beerTickerBgColorThree']
        settingsCandidate.beer_ticker_bg_color_four = userSettings['beerTickerBgColorFour']
        settingsCandidate.beer_ticker_bg_color_five = userSettings['beerTickerBgColorFive']
        settingsCandidate.beer_ticker_bg_color_direction = userSettings['beerTickerBgColorDirection']

        settingsCandidate.beer_ticker_beernames_font = userSettings['beerTickerBeernamesFont']
        settingsCandidate.beer_ticker_font = userSettings['beerTickerFont']
        settingsCandidate.beer_ticker_font_color = userSettings['beerTickerFontColor']
        settingsCandidate.beer_ticker_font_size = userSettings['beerTickerFontSize']
        settingsCandidate.beer_ticker_font_bold_toggle = userSettings['beerTickerFontBoldToggle']
        settingsCandidate.beer_ticker_font_italic_toggle = userSettings['beerTickerFontItalicToggle']
        settingsCandidate.beer_ticker_font_underline_toggle = userSettings['beerTickerFontUnderlineToggle']

        settingsCandidate.beer_ticker_toggle = userSettings['beerTickerToggle']
        settingsCandidate.beer_ticker_scroll_speed = userSettings['beerTickerScrollSpeed']

        settingsCandidate.beer_settings_screen_id = userSettings['beerSettingsScreenId']
        settingsCandidate.beer_screen_template = userSettings['beerscreenTemplate']
        settingsCandidate.beer_screen_landscape_portrait_toggle = userSettings['beerscreenLandscapePortraitToggle']

        db.session.commit()

        # templateName = _getTemplateName(userSettings['screen_template'])
        # nameFontSize = _getNameFontSize(current_user.id, Font_size_option.id)
        # styleFontSize = _getStyleFontSize(current_user.id, Font_size_option.id)
        # abvFontSize = _getAbvFontSize(current_user.id, Font_size_option.id)
        # ibuFontSize = _getIbuFontSize(current_user.id, Font_size_option.id)
        # breweryFontSize = _getBreweryFontSize(current_user.id, Font_size_option.id)
        #
        # userSettings['template_name'] = templateName
        # userSettings['nameFontSize'] = nameFontSize
        # userSettings['styleFontSize'] = styleFontSize
        # userSettings['abvFontSize'] = abvFontSize
        # userSettings['ibuFontSize'] = ibuFontSize
        # userSettings['breweryFontSize'] = breweryFontSize

        settings = {
            # "beers":beerlist,
            # "events":events,
            # "userSettings":userSettings,
            "venue_db_id": userSettings['venue_db_id'],
            "updated": True,
        }

        #######################################
        #PUSHER
        pusher_client.trigger('my-event-channel', 'new-event', {'message': settings})
        #PUSHER
        #######################################

        flash('Beerscreen Settings Updated', 'success')
        return redirect(url_for('settttings.beerscreen_settings'))

    if request.method == 'GET':
        print('```````````````````````````````````````````````````')
        print('```````````````````````````````````````````````````')
        print('settings.routes.py line 339 THIS COULD BE A PROBLEM')
        print('```````````````````````````````````````````````````')
        print('```````````````````````````````````````````````````')
        print(form['beerSettingsScreenId'])
        print(form.beerBomNameFontSize.data)
        form.beerTickerFontSize.data = settings['beerTickerFontSize']
        return render_template('beerscreen_settings.html', title='Beerscreen settings', currentUserId=current_user.id, form=form, settings=settings)

    return render_template('beerscreen_settings.html', title='Beerscreen settings', currentUserId=current_user.id, form=form, settings=settings)


# beerscreen_settings page
@settttings.route('/winescreen_settings', methods=['GET', 'POST'])
@login_required
def winescreen_settings():
    form = winescreenSettingsForm(request.form)

    # beerlist = _getCurrentBeerlist(current_user.id)
    # events = _getEventsSortAsc(current_user.id)
    settings = _getWineSettings(current_user.id)

    print(settings)

    form = WinecreenSettingsForm(request.form,
        wineNameFont = settings['wine_name_font'],
        wineNameFontColor = settings['wine_name_font_color'],
        wineNameFontSize = settings['wineNameFontSize'],
        wineNameFontBoldToggle = settings['wine_name_font_bold_toggle'],
        wineNameFontItalicToggle = settings['wine_name_font_italic_toggle'],
        wineNameFontUnderlineToggle = settings['wine_name_font_underline_toggle'],

        wineLocationFont = settings['wine_location_font'],
        wineLocationFontColor = settings['wine_location_font_color'],
        wineLocationFontSize = settings['wineLocationFontSize'],
        wineLocationFontBoldToggle = settings['wine_location_font_bold_toggle'],
        wineLocationFontItalicToggle = settings['wine_location_font_italic_toggle'],
        wineLocationFontUnderlineToggle = settings['wine_location_font_underline_toggle'],

        wineDescriptionFont = settings['wine_description_font'],
        wineDescriptionFontColor = settings['wine_description_font_color'],
        wineDescriptionFontSize = settings['wineDescriptionFontSize'],
        wineDescriptionFontBoldToggle = settings['wine_description_font_bold_toggle'],
        wineDescriptionFontItalicToggle = settings['wine_description_font_italic_toggle'],
        wineDescriptionFontUnderlineToggle = settings['wine_description_font_underline_toggle'],

        wineGlassFont = settings['wine_glass_font'],
        wineGlassFontColor = settings['wine_glass_font_color'],
        wineGlassFontSize = settings['wineGlassFontSize'],
        wineGlassFontBoldToggle = settings['wine_glass_font_bold_toggle'],
        wineGlassFontItalicToggle = settings['wine_glass_font_italic_toggle'],
        wineGlassFontUnderlineToggle = settings['wine_glass_font_underline_toggle'],

        wineBottleFont = settings['wine_bottle_font'],
        wineBottleFontColor = settings['wine_bottle_font_color'],
        wineBottleFontSize = settings['wineBottleFontSize'],
        wineBottleFontBoldToggle = settings['wine_bottle_font_bold_toggle'],
        wineBottleFontItalicToggle = settings['wine_bottle_font_italic_toggle'],
        wineBottleFontUnderlineToggle = settings['wine_bottle_font_underline_toggle'],

        wineVarietalFont = settings['wine_varietal_font'],
        wineVarietalFontColor = settings['wine_varietal_font_color'],
        wineVarietalFontSize = settings['wineVarietalFontSize'],
        wineVarietalFontBoldToggle = settings['wine_varietal_font_bold_toggle'],
        wineVarietalFontItalicToggle = settings['wine_varietal_font_italic_toggle'],
        wineVarietalFontUnderlineToggle = settings['wine_varietal_font_underline_toggle'],

        wineTypeFont = settings['wine_type_font'],
        wineTypeFontColor = settings['wine_type_font_color'],
        wineTypeFontSize = settings['wineTypeFontSize'],
        wineTypeFontBoldToggle = settings['wine_type_font_bold_toggle'],
        wineTypeFontItalicToggle = settings['wine_type_font_italic_toggle'],
        wineTypeFontUnderlineToggle = settings['wine_type_font_underline_toggle'],

        wineFoodPairingsFont = settings['wine_foodPairings_font'],
        wineFoodPairingsFontColor = settings['wine_foodPairings_font_color'],
        wineFoodPairingsFontSize = settings['wineFoodPairingsFontSize'],
        wineFoodPairingsFontBoldToggle = settings['wine_foodPairings_font_bold_toggle'],
        wineFoodPairingsFontItalicToggle = settings['wine_foodPairings_font_italic_toggle'],
        wineFoodpairingsFontUnderlineToggle = settings['wine_foodPairings_font_underline_toggle'],

        wineWebsiteFont = settings['wine_website_font'],
        wineWebsiteFontColor = settings['wine_website_font_color'],
        wineWebsiteFontSizeHTML = settings['wineWebsiteFontSize'],
        wineWebsiteFontBoldToggle = settings['wine_website_font_bold_toggle'],
        wineWebsiteFontItalicToggle = settings['wine_website_font_italic_toggle'],
        wineWebsiteFontUnderlineToggle = settings['wine_website_font_underline_toggle'],

        wineTickerBgColorOne = settings['wine_ticker_bg_color_one'],
        wineTickerBgColorTwo = settings['wine_ticker_bg_color_two'],
        wineTickerBgColorThree = settings['wine_ticker_bg_color_three'],
        wineTickerBgColorFour = settings['wine_ticker_bg_color_four'],
        wineTickerBgColorFive = settings['wine_ticker_bg_color_five'],
        wineTickerBgColorDirection = settings['wine_ticker_bg_color_direction'],
        wineTickerBeernamesFont = settings['wine_ticker_beernames_font'],
        wineTickerFont = settings['wine_ticker_font'],
        wineTickerFontColor = settings['wine_ticker_font_color'],
        wineTickerFontSizeHTML = settings['wineTickerFontSize'],
        wineTickerFontBoldToggle = settings['wine_ticker_font_bold_toggle'],
        wineTickerFontItalicToggle = settings['wine_ticker_font_italic_toggle'],
        wineTickerFontUnderlineToggle = settings['wine_ticker_font_underline_toggle'],

        wineTickerToggle = settings['wine_ticker_toggle'],
        wineTickerScrollSpeed = settings['wine_ticker_scroll_speed'],

        eventNameFont = settings['event_name_font'],
        eventNameFontColor = settings['event_name_font_color'],
        eventNameFontSizeHTML = settings['eventNameFontSize'],
        eventNameFontBoldToggle = settings['event_name_font_bold_toggle'],
        eventNameFontItalicToggle = settings['event_name_font_italic_toggle'],
        eventNameFontUnderlineToggle = settings['event_name_font_underline_toggle'],

        eventArtistFont = settings['event_artist_font'],
        eventArtistFontColor = settings['event_artist_font_color'],
        eventArtistFontSizeHTML = settings['eventArtistFontSize'],
        eventArtistFontBoldToggle = settings['event_artist_font_bold_toggle'],
        eventArtistFontItalicToggle = settings['event_artist_font_italic_toggle'],
        eventArtistFontUnderlineToggle = settings['event_artist_font_underline_toggle'],

        eventDateofeventFont = settings['event_date_of_event_font'],
        eventDateofeventFontColor = settings['event_date_of_event_font_color'],
        eventDateofeventFontSizeHTML = settings['eventDateofeventFontSize'],
        eventDateofeventFontBoldToggle = settings['event_date_of_event_font_bold_toggle'],
        eventDateofeventFontItalicToggle = settings['event_date_of_event_font_italic_toggle'],
        eventDateofeventFontUnderlineToggle = settings['event_date_of_event_font_underline_toggle'],

        eventStarttimeFont = settings['event_starttime_font'],
        eventStarttimeFontColor = settings['event_starttime_font_color'],
        eventStarttimeFontSizeHTML = settings['eventStarttimeFontSize'],
        eventStarttimeFontBoldToggle = settings['event_starttime_font_bold_toggle'],
        eventStarttimeFontItalicToggle = settings['event_starttime_font_italic_toggle'],
        eventStarttimeFontUnderlineToggle = settings['event_starttime_font_underline_toggle'],

        eventEndtimeFont = settings['event_endtime_font'],
        eventEndtimeFontColor = settings['event_endtime_font_color'],
        eventEndtimeFontSizeHTML = settings['eventEndtimeFontSize'],
        eventEndtimeFontBoldToggle = settings['event_endtime_font_bold_toggle'],
        eventEndtimeFontItalicToggle = settings['event_endtime_font_italic_toggle'],
        eventEndtimeFontUnderlineToggle = settings['event_endtime_font_underline_toggle'],

        eventLocationFont = settings['event_location_font'],
        eventLocationFontColor = settings['event_location_font_color'],
        eventLocationFontSizeHTML = settings['eventLocationFontSize'],
        eventLocationFontBoldToggle = settings['event_location_font_bold_toggle'],
        eventLocationFontItalicToggle = settings['event_location_font_italic_toggle'],
        eventLocationFontUnderlineToggle = settings['event_location_font_underline_toggle'],

        eventTickerBgColorOne = settings['event_ticker_bg_color_one'],
        eventTickerBgColorTwo = settings['event_ticker_bg_color_two'],
        eventTickerBgColorThree = settings['event_ticker_bg_color_three'],
        eventTickerBgColorFour = settings['event_ticker_bg_color_four'],
        eventTickerBgColorFive = settings['event_ticker_bg_color_five'],
        eventTickerBgColorDirection = settings['event_ticker_bg_color_direction'],
        eventTickerBeernamesFont = settings['event_ticker_beernames_font'],
        eventTickerFont = settings['event_ticker_font'],
        eventTickerFontColor = settings['event_ticker_font_color'],
        eventTickerFontSizeHTML = settings['eventTickerFontSize'],
        eventTickerFontBoldToggle = settings['event_ticker_font_bold_toggle'],
        eventTickerFontItalicToggle = settings['event_ticker_font_italic_toggle'],
        eventTickerFontUnderlineToggle = settings['event_ticker_font_underline_toggle'],

        eventTickerToggle = settings['event_ticker_toggle'],
        eventTickerScrollSpeed = settings['event_ticker_scroll_speed'],

        itemNameFont = settings['item_name_font'],
        itemNameFontColor = settings['item_name_font_color'],
        itemNameFontSizeHTML = settings['itemNameFontSize'],
        itemNameFontBoldToggle = settings['item_name_font_bold_toggle'],
        itemNameFontItalicToggle = settings['item_name_font_italic_toggle'],
        itemNameFontUnderlineToggle = settings['item_name_font_underline_toggle'],

        itemDescriptionFont = settings['item_description_font'],
        itemDescriptionFontColor = settings['item_description_font_color'],
        itemDescriptionFontSizeHTML = settings['itemDescriptionFontSize'],
        itemDescriptionFontBoldToggle = settings['item_description_font_bold_toggle'],
        itemDescriptionFontItalicToggle = settings['item_description_font_italic_toggle'],
        itemDescriptionFontUnderlineToggle = settings['item_description_font_underline_toggle'],

        itemPriceFont = settings['item_price_font'],
        itemPriceFontColor = settings['item_price_font_color'],
        itemPriceFontSizeHTML = settings['itemPriceFontSize'],
        itemPriceFontBoldToggle = settings['item_price_font_bold_toggle'],
        itemPriceFontItalicToggle = settings['item_price_font_italic_toggle'],
        itemPriceFontUnderlineToggle = settings['item_price_font_underline_toggle'],

        itemTickerBgColorOne = settings['item_ticker_bg_color_one'],
        itemTickerBgColorTwo = settings['item_ticker_bg_color_two'],
        itemTickerBgColorThree = settings['item_ticker_bg_color_three'],
        itemTickerBgColorFour = settings['item_ticker_bg_color_four'],
        itemTickerBgColorFive = settings['item_ticker_bg_color_five'],
        itemTickerBgColorDirection = settings['item_ticker_bg_color_direction'],
        itemTickerBeernamesFont = settings['item_ticker_beernames_font'],
        itemTickerFont = settings['item_ticker_font'],
        itemTickerFontColor = settings['item_ticker_font_color'],
        itemTickerFontSizeHTML = settings['itemTickerFontSize'],
        itemTickerFontBoldToggle = settings['item_ticker_font_bold_toggle'],
        itemTickerFontItalicToggle = settings['item_ticker_font_italic_toggle'],
        itemTickerFontUnderlineToggle = settings['item_ticker_font_underline_toggle'],

        itemTickerToggle = settings['item_ticker_toggle'],
        itemTickerScrollSpeed = settings['item_ticker_scroll_speed'],

        settingsScreenId = settings['settings_screen_id'],
        screenTemplate = settings['screen_template'],
        venueDbId = settings['venue_db_id'],
        templateName = settings['template_name'],
    )

    numOfScreens = []
    for x in range(1, 2, 1):
        number = {
            "id":x,
            "number":x,
        }
        numOfScreens.append(number)
    screenNumSettings = numOfScreens
    directions = [
        {
            "id":"to bottom",
            "direction":"to bottom",
        },
        {
            "id":"to top",
            "direction":"to top",
        },
        {
            "id":"to left",
            "direction":"to left",
        },
        {
            "id":"to right",
            "direction":"to right",
        },
        {
            "id":"to bottom left",
            "direction":"to bottom left",
        },
        {
            "id":"to bottom right",
            "direction":"to bottom right",
        },
        {
            "id":"to top left",
            "direction":"to left",
        },
        {
            "id":"to top right",
            "direction":"to top right",
        },
    ]

    # function called from this module to query font size table
    sizes = _getFontSizes(current_user.id)
    # function called from this module to query template table
    templates = _getTemplates(current_user.id)

    form.numberOfScreens.choices = [ (number['id'], number['number']) for number in numOfScreens ]
    form.screenSettingsId.choices = [ (number['id'], number['number']) for number in screenNumSettings ]

    form.fontColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.shadowFontColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.backgroundColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]

    form.nameFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.styleFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.abvFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.ibuFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.breweryFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]
    form.screenTemplate.choices = [ (template['id'], template['template_name']) for template in templates ]

    if form.validate_on_submit():
        userSettings = {}
        userSettings['number_of_screens'] = form.numberOfScreens.data
        userSettings['beerscreen_settings_id'] = form.beerscreenSettingsId.data
        userSettings['font_color_one'] = form.fontColorOne.data
        userSettings['font_color_two'] = form.fontColorTwo.data
        userSettings['font_color_three'] = form.fontColorThree.data
        userSettings['font_color_direction'] = form.fontColorDirection.data
        userSettings['shadow_font_color_one'] = form.shadowFontColorOne.data
        userSettings['shadow_font_color_two'] = form.shadowFontColorTwo.data
        userSettings['shadow_font_color_three'] = form.shadowFontColorThree.data
        userSettings['shadow_font_color_direction'] = form.shadowFontColorDirection.data
        userSettings['background_color_one'] = form.backgroundColorOne.data
        userSettings['background_color_two'] = form.backgroundColorTwo.data
        userSettings['background_color_three'] = form.backgroundColorThree.data
        userSettings['background_color_direction'] = form.backgroundColorDirection.data
        userSettings['name_font_color'] = form.nameFontColor.data
        userSettings['style_font_color'] = form.styleFontColor.data
        userSettings['abv_font_color'] = form.abvFontColor.data
        userSettings['ibu_font_color'] = form.ibuFontColor.data
        userSettings['brewery_font_color'] = form.breweryFontColor.data
        userSettings['name_font_size'] = form.nameFontSize.data
        userSettings['style_font_size'] = form.styleFontSize.data
        userSettings['abv_font_size'] = form.abvFontSize.data
        userSettings['ibu_font_size'] = form.ibuFontSize.data
        userSettings['brewery_font_size'] = form.breweryFontSize.data
        userSettings['screen_template'] = form.screenTemplate.data
        userSettings['ticker_toggle'] = form.tickerToggle.data
        userSettings['ticker_scroll_speed'] = form.tickerScrollSpeed.data
        userSettings['venue_db_id'] = current_user.id

        settingsCandidate = User_settings.query.filter_by(beerscreen_settings_id=userSettings['beerscreen_settings_id'], venue_db_id=current_user.id).first()

        settingsCandidate.number_of_screens = userSettings['number_of_screens']
        settingsCandidate.beerscreen_settings_id = userSettings['beerscreen_settings_id']
        settingsCandidate.font_color_one = userSettings['font_color_one']
        settingsCandidate.font_color_two = userSettings['font_color_two']
        settingsCandidate.font_color_three = userSettings['font_color_three']
        settingsCandidate.font_color_direction = userSettings['font_color_direction']
        settingsCandidate.shadow_font_color_one = userSettings['shadow_font_color_one']
        settingsCandidate.shadow_font_color_two = userSettings['shadow_font_color_two']
        settingsCandidate.shadow_font_color_three = userSettings['shadow_font_color_three']
        settingsCandidate.shadow_font_color_direction = userSettings['shadow_font_color_direction']
        settingsCandidate.background_color_one = userSettings['background_color_one']
        settingsCandidate.background_color_two = userSettings['background_color_two']
        settingsCandidate.background_color_three = userSettings['background_color_three']
        settingsCandidate.background_color_direction = userSettings['background_color_direction']
        settingsCandidate.name_font_color = userSettings['name_font_color']
        settingsCandidate.style_font_color = userSettings['style_font_color']
        settingsCandidate.abv_font_color = userSettings['abv_font_color']
        settingsCandidate.ibu_font_color = userSettings['ibu_font_color']
        settingsCandidate.brewery_font_color = userSettings['brewery_font_color']
        settingsCandidate.name_font_size = userSettings['name_font_size']
        settingsCandidate.style_font_size = userSettings['style_font_size']
        settingsCandidate.abv_font_size = userSettings['abv_font_size']
        settingsCandidate.ibu_font_size = userSettings['ibu_font_size']
        settingsCandidate.brewery_font_size = userSettings['brewery_font_size']
        settingsCandidate.screen_template = userSettings['screen_template']
        settingsCandidate.ticker_toggle = userSettings['ticker_toggle']
        settingsCandidate.ticker_scroll_speed = userSettings['ticker_scroll_speed']
        db.session.commit()

        templateName = _getTemplateName(userSettings['screen_template'])
        nameFontSize = _getNameFontSize(current_user.id, Font_size_option.id)
        styleFontSize = _getStyleFontSize(current_user.id, Font_size_option.id)
        abvFontSize = _getAbvFontSize(current_user.id, Font_size_option.id)
        ibuFontSize = _getIbuFontSize(current_user.id, Font_size_option.id)
        breweryFontSize = _getBreweryFontSize(current_user.id, Font_size_option.id)

        userSettings['template_name'] = templateName
        userSettings['nameFontSize'] = nameFontSize
        userSettings['styleFontSize'] = styleFontSize
        userSettings['abvFontSize'] = abvFontSize
        userSettings['ibuFontSize'] = ibuFontSize
        userSettings['breweryFontSize'] = breweryFontSize

        settings = {
            # "beers":beerlist,
            # "events":events,
            "userSettings":userSettings,
            "updated": True,
        }

        #######################################
        #PUSHER
        pusher_client.trigger('my-event-channel', 'new-event', {'message': settings})
        #PUSHER
        #######################################

        flash('Settings Updated', 'success')
        return redirect(url_for('settttings.settings'))
    return render_template('settings.html', title='Settings', form=form, settings=settings)
