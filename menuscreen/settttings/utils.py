from flask_login import current_user
from menuscreen import db
from menuscreen.models import User, User_settings, Font_size_options, Template

def _getFontSizes(user_id):
    user = User.query.filter_by(id=user_id).first()
    datas = user.font_size_options
    sizes = []
    for data in datas:
        size = {
            "id":data.id,
            "font_sizes":data.font_sizes,
        }
        sizes.append(size)
    # print('******************* FONT SIZE OPTIONS *******************')
    # print('type(sizes): {}'.format(type(sizes)))
    # print('sizes: {}'.format(sizes))
    # print('******************* FONT SIZE OPTIONS *******************')
    return sizes

def _getTemplates(user_id):
    user = User.query.filter_by(id=user_id).first()
    datas = user.templates
    templates = []
    for data in datas:
        template = {
            "id":data.id,
            "template_name":data.template_name,
            "screen_number":data.screen_number,
            "active_template":data.active_template,
        }
        templates.append(template)
    # print('******************* TEMPLATES *******************')
    # print('type(templates): {}'.format(type(templates)))
    # print('templates: {}'.format(templates))
    # print('******************* TEMPLATES *******************')
    return templates

def _getTemplateName(template_id):
    template = Template.query.filter_by(id=template_id).first()
    return template.template_name

def _getNameFontSize(user_id, fontSizeOptions):
    nameFontSize = db.session.query(
    Font_size_options.font_sizes
    ).join(User_settings, User_settings.name_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return nameFontSize

def _getStyleFontSize(user_id, fontSizeOptions):
    styleFontSize = db.session.query(
    Font_size_options.font_sizes
    ).join(User_settings, User_settings.name_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return styleFontSize

def _getAbvFontSize(user_id, fontSizeOptions):
    abvFontSize = db.session.query(
    Font_size_options.font_sizes
    ).join(User_settings, User_settings.abv_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return abvFontSize

def _getIbuFontSize(user_id, fontSizeOptions):
    ibuFontSize = db.session.query(
    Font_size_options.font_sizes
    ).join(User_settings, User_settings.ibu_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return ibuFontSize

def _getBreweryFontSize(user_id, fontSizeOptions):
    breweryFontSize = db.session.query(
    Font_size_options.font_sizes
    ).join(User_settings, User_settings.brewery_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return breweryFontSize

def _getSettings(user_id):
    settings_db = User_settings.query.filter_by(venue_db_id=current_user.id).first()
    settings_db = db.session.query(
        User_settings.number_of_screens,
        User_settings.beerscreen_settings_id,
        User_settings.font_color_one,
        User_settings.font_color_two,
        User_settings.font_color_three,
        User_settings.font_color_direction,
        User_settings.shadow_font_color_one,
        User_settings.shadow_font_color_two,
        User_settings.shadow_font_color_three,
        User_settings.shadow_font_color_direction,
        User_settings.background_color_one,
        User_settings.background_color_two,
        User_settings.background_color_three,
        User_settings.background_color_direction,
        User_settings.name_font_color,
        User_settings.style_font_color,
        User_settings.abv_font_color,
        User_settings.ibu_font_color,
        User_settings.brewery_font_color,
        User_settings.name_font_size,
        User_settings.style_font_size,
        User_settings.abv_font_size,
        User_settings.ibu_font_size,
        User_settings.brewery_font_size,
        User_settings.screen_template,
        User_settings.ticker_toggle,
        User_settings.ticker_scroll_speed,
        User_settings.venue_db_id,
        Template.template_name,
        Font_size_options.font_sizes,
    ).join(Template, User_settings.screen_template == Template.id
    ).join(Font_size_options, User_settings.name_font_size  == Font_size_options.id
    ).filter(User_settings.venue_db_id == current_user.id
    ).first()

    nameFontSize = db.session.query(
        User_settings.name_font_size,
        Font_size_options.font_sizes,
    ).join(Font_size_options, User_settings.name_font_size == Font_size_options.id
    ).filter(User_settings.venue_db_id == current_user.id
    ).first()

    styleFontSize = db.session.query(
        User_settings.name_font_size,
        Font_size_options.font_sizes,
    ).join(Font_size_options, User_settings.style_font_size == Font_size_options.id
    ).filter(User_settings.venue_db_id == current_user.id
    ).first()

    abvFontSize = db.session.query(
        User_settings.abv_font_size,
        Font_size_options.font_sizes,
    ).join(Font_size_options, User_settings.abv_font_size == Font_size_options.id
    ).filter(User_settings.venue_db_id == current_user.id
    ).first()

    ibuFontSize = db.session.query(
        User_settings.ibu_font_size,
        Font_size_options.font_sizes,
    ).join(Font_size_options, User_settings.ibu_font_size == Font_size_options.id
    ).filter(User_settings.venue_db_id == current_user.id
    ).first()
    breweryFontSize = db.session.query(
        User_settings.brewery_font_size,
        Font_size_options.font_sizes,
    ).join(Font_size_options, User_settings.brewery_font_size == Font_size_options.id
    ).filter(User_settings.venue_db_id == current_user.id
    ).first()

    this_setting = {
        "numberOfScreens" : settings_db.number_of_screens,
        "beerscreenSettingsId" : settings_db.beerscreen_settings_id,
        "fontColorOne" : settings_db.font_color_one,
        "fontColorTwo" : settings_db.font_color_two,
        "fontColorThree" : settings_db.font_color_three,
        "fontColorDirection" : settings_db.font_color_direction,
        "shadowFontColorOne" : settings_db.shadow_font_color_one,
        "shadowFontColorTwo" : settings_db.shadow_font_color_two,
        "shadowFontColorThree" : settings_db.shadow_font_color_three,
        "shadowFontColorDirection" : settings_db.shadow_font_color_direction,
        "backgroundColorOne" : settings_db.background_color_one,
        "backgroundColorTwo" : settings_db.background_color_two,
        "backgroundColorThree" : settings_db.background_color_three,
        "backgroundColorDirection" : settings_db.background_color_direction,
        "nameFontColor" : settings_db.name_font_color,
        "styleFontColor" : settings_db.style_font_color,
        "abvFontColor" : settings_db.abv_font_color,
        "ibuFontColor" : settings_db.ibu_font_color,
        "breweryFontColor" : settings_db.brewery_font_color,
        "nameFontSizeHTML" : nameFontSize.font_sizes,
        "styleFontSizeHTML" : styleFontSize.font_sizes,
        "abvFontSizeHTML" : abvFontSize.font_sizes,
        "ibuFontSizeHTML" : ibuFontSize.font_sizes,
        "breweryFontSizeHTML" : breweryFontSize.font_sizes,

        "nameFontSize" :settings_db.name_font_size,
        "styleFontSize" : settings_db.style_font_size,
        "abvFontSize" : settings_db.abv_font_size,
        "ibuFontSize" : settings_db.ibu_font_size,
        "breweryFontSize" : settings_db.brewery_font_size,

        "screenTemplate" : settings_db.screen_template,
        "tickerToggle" : settings_db.ticker_toggle,
        "tickerScrollSpeed" : settings_db.ticker_scroll_speed,
        "venue_db_id" : settings_db.venue_db_id,
        "templateName" : settings_db.template_name,
    }
    return this_setting
