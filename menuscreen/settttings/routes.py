from flask import (render_template, url_for, flash, redirect,
                    request, abort, jsonify, Blueprint)
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import User, Beerscreen_settings, Winescreen_settings, Eventscreen_settings, Itemscreen_settings, Font_size_options, Template
from menuscreen.settttings.forms import BeerscreenSettingsForm, WinescreenSettingsForm, EventscreenSettingsForm, ItemscreenSettingsForm, FontSizeForm, TemplateForm
from menuscreen.settttings.utils import _getFontSizes, _getTemplates, _getBeerSettings, _getNameFontSize, _getStyleFontSize, _getTemplateName, _getAbvFontSize, _getIbuFontSize, _getBreweryFontSize
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

# beerscreen_settings page
@settttings.route('/beerscreen_settings', methods=['GET', 'POST'])
@login_required
def beerscreen_settings():
    form = BeerscreenSettingsForm(request.form)

    # beerlist = _getCurrentBeerlist(current_user.id)
    # events = _getEventsSortAsc(current_user.id)
    settings = _getBeerSettings(current_user.id)

    print(settings)

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
        beerBomBreweryFontColof = settings['beerBomBreweryFontColof'],
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
    fonts = [
        {
            "id" : "Times Roman",
            "font" : "Times Roman"
        },
        {
            "id" : "Courier New",
            "font" : "Courier New"
        }
    ]

    # function called from this module to query font size table
    sizes = _getFontSizes(current_user.id)
    # function called from this module to query template table
    templates = _getTemplates(current_user.id)

    form.beerSettingsScreenId.choices = [ (number['id'], number['number']) for number in screenNumSettings ]

    form.fontColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.shadowFontColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]
    form.beerBomBgColorDirection.choices = [ (direction['id'], direction['direction']) for direction in directions ]

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
    form.beerTickerFontSize.choices = [ (size['id'], size['font_sizes']) for size in sizes ]



    form.beerscreenTemplate.choices = [ (template['id'], template['template_name']) for template in templates ]

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

        flash('Beerscreen Settings Updated', 'success')
        return redirect(url_for('settttings.beerscreen_settings'))
    return render_template('beerscreen_settings.html', title='Settings', form=form, settings=settings)


# beerscreen_settings page
@settttings.route('/winescreen_settings', methods=['GET', 'POST'])
@login_required
def winescreen_settings():
    form = winescreenSettingsForm(request.form)

    # beerlist = _getCurrentBeerlist(current_user.id)
    # events = _getEventsSortAsc(current_user.id)
    settings = _getWineSettings(current_user.id)

    print(settings)

    form = WinescreenSettingsForm(request.form,
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
