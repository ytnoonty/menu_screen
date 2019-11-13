from flask import (render_template, url_for, flash, redirect,
                    request, abort, jsonify, Blueprint)
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import User, User_settings, Font_size_options, Template
from menuscreen.settttings.forms import SettingsForm, FontSizeForm, TemplateForm
from menuscreen.settttings.utils import _getFontSizes, _getTemplates, _getSettings, _getNameFontSize, _getStyleFontSize, _getTemplateName, _getAbvFontSize, _getIbuFontSize, _getBreweryFontSize
from menuscreen.list_history.utils import _getCurrentBeerlist
from menuscreen.event.utils import _getEventsSortAsc
from menuscreen.users.init_db_tables import getVenueId

from menuscreen import pusher_client

settttings = Blueprint('settttings', __name__)

# GET USER SETTINGS
@settttings.route('/_get_screen_settings', methods=['GET', 'POST'])
# @login_required
def _get_screen_settings():
    data = request.get_json()
    print("**************************************")
    print("**************************************")
    print("list_history. /_get_screen_settings")
    print(data)
    if (data):
        current_user_id = getVenueId(data['userName'])
        print("NOT LOGGED IN")
        print(data['userName'])
        print(current_user_id)
        data = _getSettings(current_user_id)
    elif (current_user.is_authenticated):
        print("LOGGED IN")
        print(current_user.id)
        data = _getSettings(current_user.id)
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
        newFontSize = Font_size_options(font_sizes=fontSize, venue_db_id=current_user.id)
        db.session.add(newFontSize)
        db.session.commit()
        flash('New Font size has been added!', 'success')
        return redirect(url_for('settttings.add_font_size'))
    return render_template('add_font_size.html', title='Edit Font Sizes', legend='Edit Font Size List', form=form)

# Settings page
@settttings.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm(request.form)

    beerlist = _getCurrentBeerlist(current_user.id)
    events = _getEventsSortAsc(current_user.id)
    settings = _getSettings(current_user.id)

    print(settings)

    form = SettingsForm(request.form,
        numberOfScreens = settings['numberOfScreens'],
        beerscreenSettingsId = settings['beerscreenSettingsId'],
        fontColorOne = settings['fontColorOne'],
        fontColorTwo = settings['fontColorTwo'],
        fontColorThree = settings['fontColorThree'],
        fontColorDirection = settings['fontColorDirection'],
        shadowFontColorOne = settings['shadowFontColorOne'],
        shadowFontColorTwo = settings['shadowFontColorTwo'],
        shadowFontColorThree = settings['shadowFontColorThree'],
        shadowFontColorDirection = settings['shadowFontColorDirection'],
        backgroundColorOne = settings['backgroundColorOne'],
        backgroundColorTwo = settings['backgroundColorTwo'],
        backgroundColorThree = settings['backgroundColorThree'],
        backgroundColorDirection = settings['backgroundColorDirection'],
        nameFontColor = settings['nameFontColor'],
        styleFontColor = settings['styleFontColor'],
        abvFontColor = settings['abvFontColor'],
        ibuFontColor = settings['ibuFontColor'],
        breweryFontColor = settings['breweryFontColor'],
        nameFontSize = settings['nameFontSize'],
        styleFontSize = settings['styleFontSize'],
        abvFontSize = settings['abvFontSize'],
        ibuFontSize = settings['ibuFontSize'],
        breweryFontSize = settings['breweryFontSize'],
        screenTemplate = settings['screenTemplate'],
        tickerToggle = settings['tickerToggle'],
        tickerScrollSpeed = settings['tickerScrollSpeed']
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
        }
    ]

    # function called from this module to query font size table
    sizes = _getFontSizes(current_user.id)
    # function called from this module to query template table
    templates = _getTemplates(current_user.id)

    form.numberOfScreens.choices = [ (number['id'], number['number']) for number in numOfScreens ]
    form.beerscreenSettingsId.choices = [ (number['id'], number['number']) for number in screenNumSettings ]

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
        nameFontSize = _getNameFontSize(current_user.id, Font_size_options.id)
        styleFontSize = _getStyleFontSize(current_user.id, Font_size_options.id)
        abvFontSize = _getAbvFontSize(current_user.id, Font_size_options.id)
        ibuFontSize = _getIbuFontSize(current_user.id, Font_size_options.id)
        breweryFontSize = _getBreweryFontSize(current_user.id, Font_size_options.id)

        userSettings['template_name'] = templateName
        userSettings['nameFontSize'] = nameFontSize
        userSettings['styleFontSize'] = styleFontSize
        userSettings['abvFontSize'] = abvFontSize
        userSettings['ibuFontSize'] = ibuFontSize
        userSettings['breweryFontSize'] = breweryFontSize

        settings = {
            "beers":beerlist,
            "events":events,
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
