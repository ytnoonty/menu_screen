from flask_login import current_user
from menuscreen import db
from menuscreen.models import (User, List_history, Beerscreen_setting, Winecreen_setting,
                            Eventscreen_setting, Itemscreen_setting,
                            Font_size_option, Template, Drink_size, Drink_price)

def _getBeerSize1(userId, beer_id):
    size = db.session.query(
        List_history.id,
        Drink_size.drink_size,
    ).outerjoin(Drink_size, List_history.size_id_1 == Drink_size.id
    ).filter(Drink_size.venue_db_id == userId
    ).first()
    return size.drink_size
def _getBeerSize2(userId, beer_id):
    size = db.session.query(
        List_history.id,
        Drink_size.drink_size,
    ).outerjoin(Drink_size, List_history.size_id_2 == Drink_size.id
    ).filter(Drink_size.venue_db_id == userId
    ).first()
    return size.drink_size
def _getBeerSize3(userId, beer_id):
    size = db.session.query(
        List_history.id,
        Drink_size.drink_size,
    ).outerjoin(Drink_size, List_history.size_id_3 == Drink_size.id
    ).filter(Drink_size.venue_db_id == userId
    ).first()
    return size.drink_size
def _getBeerSize4(userId, beer_id):
    size = db.session.query(
        List_history.id,
        Drink_size.drink_size,
    ).outerjoin(Drink_size, List_history.size_id_4 == Drink_size.id
    ).filter(Drink_size.venue_db_id == userId
    ).first()
    return size.drink_size

def _getBeerPrice1(userId, beer_id):
    price = db.session.query(
        List_history.id,
        Drink_price.drink_price,
    ).join(Drink_price, List_history.price_id_1 == Drink_price.id
    ).filter(List_history.venue_db_id == userId
    ).first()
    return price.drink_price

def _getBeerPrice2(userId, beer_id):
    price = db.session.query(
        List_history.id,
        Drink_price.drink_price,
    ).join(Drink_price, List_history.price_id_2 == Drink_price.id
    ).filter(List_history.venue_db_id == userId
    ).first()
    return price.drink_price
def _getBeerPrice3(userId, beer_id):
    price = db.session.query(
        List_history.id,
        Drink_price.drink_price,
    ).join(Drink_price, List_history.price_id_3 == Drink_price.id
    ).filter(List_history.venue_db_id == userId
    ).first()
    return price.drink_price
def _getBeerPrice4(userId, beer_id):
    price = db.session.query(
        List_history.id,
        Drink_price.drink_price,
    ).join(Drink_price, List_history.price_id_4 == Drink_price.id
    ).filter(List_history.venue_db_id == userId
    ).first()
    return price.drink_price

def _getDrinkSizes(user_id):
    user = User.query.filter_by(id=user_id).first()
    print(user)
    datas = user.drink_size_options
    print(datas)
    sizes = []
    for data in datas:
        size = {
            "id": data.id,
            "drink_size": data.drink_size,
        }
        sizes.append(size)
    print(sizes)
    return sizes

def _getDrinkPrices(user_id):
    user = User.query.filter_by(id=user_id).first()
    print(user)
    datas = user.drink_price_options
    print(datas)
    prices = []
    for data in datas:
        price = {
            "id": data.id,
            "drink_price": data.drink_price,
        }
        prices.append(price)
    print(prices)
    return prices

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

def _getFontSizeOptions(user_id):
    user = User.query.filter_by(id=user_id).first()
    datas = user.font_size_options
    sizes = []
    for data in datas:
        sizes.append(data.font_sizes)
        # size = {
        #     "id":data.id,
        #     "font_sizes":data.font_sizes,
        # }
        # sizes.append(size)
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
    Font_size_option.font_sizes
    ).join(User_settings, User_settings.name_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return nameFontSize

def _getStyleFontSize(user_id, fontSizeOptions):
    styleFontSize = db.session.query(
    Font_size_option.font_sizes
    ).join(User_settings, User_settings.name_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return styleFontSize

def _getAbvFontSize(user_id, fontSizeOptions):
    abvFontSize = db.session.query(
    Font_size_option.font_sizes
    ).join(User_settings, User_settings.abv_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return abvFontSize

def _getIbuFontSize(user_id, fontSizeOptions):
    ibuFontSize = db.session.query(
    Font_size_option.font_sizes
    ).join(User_settings, User_settings.ibu_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return ibuFontSize

def _getBreweryFontSize(user_id, fontSizeOptions):
    breweryFontSize = db.session.query(
    Font_size_option.font_sizes
    ).join(User_settings, User_settings.brewery_font_size == fontSizeOptions
    ).filter(User_settings.venue_db_id == user_id
    ).first()
    return breweryFontSize

def _getBeerSettings(screenData):
    print("screenData: {}".format(screenData))
    userId = screenData['userId']
    displayId = screenData['screenNumber']
    # settings_db = Beerscreen_setting.query.filter_by(venue_db_id=current_user.id).first()
    # settings_db = Beerscreen_setting.query.filter_by(venue_db_id=current_user_id).first()
    settings_db = db.session.query(
        Beerscreen_setting.font_color_one,
        Beerscreen_setting.font_color_two,
        Beerscreen_setting.font_color_three,
        Beerscreen_setting.font_color_direction,
        Beerscreen_setting.shadow_font_color_one,
        Beerscreen_setting.shadow_font_color_two,
        Beerscreen_setting.shadow_font_color_three,
        Beerscreen_setting.shadow_font_color_direction,

        Beerscreen_setting.beer_bom_background_color_one,
        Beerscreen_setting.beer_bom_background_color_two,
        Beerscreen_setting.beer_bom_background_color_three,
        Beerscreen_setting.beer_bom_background_color_four,
        Beerscreen_setting.beer_bom_background_color_five,
        Beerscreen_setting.beer_bom_background_color_direction,

        Beerscreen_setting.beer_bom_name_font,
        Beerscreen_setting.beer_bom_name_font_color,
        Beerscreen_setting.beer_bom_name_font_size,
        Beerscreen_setting.beer_bom_name_font_bold_toggle,
        Beerscreen_setting.beer_bom_name_font_italic_toggle,
        Beerscreen_setting.beer_bom_name_font_underline_toggle,

        Beerscreen_setting.beer_bom_style_font,
        Beerscreen_setting.beer_bom_style_font_color,
        Beerscreen_setting.beer_bom_style_font_size,
        Beerscreen_setting.beer_bom_style_font_bold_toggle,
        Beerscreen_setting.beer_bom_style_font_italic_toggle,
        Beerscreen_setting.beer_bom_style_font_underline_toggle,

        Beerscreen_setting.beer_bom_abv_font_color,
        Beerscreen_setting.beer_bom_abv_font_size,
        Beerscreen_setting.beer_bom_abv_font_bold_toggle,
        Beerscreen_setting.beer_bom_abv_font_italic_toggle,
        Beerscreen_setting.beer_bom_abv_font_underline_toggle,

        Beerscreen_setting.beer_bom_ibu_font_color,
        Beerscreen_setting.beer_bom_ibu_font_size,
        Beerscreen_setting.beer_bom_ibu_font_bold_toggle,
        Beerscreen_setting.beer_bom_ibu_font_italic_toggle,
        Beerscreen_setting.beer_bom_ibu_font_underline_toggle,

        Beerscreen_setting.beer_bom_brewery_font,
        Beerscreen_setting.beer_bom_brewery_font_color,
        Beerscreen_setting.beer_bom_brewery_font_size,
        Beerscreen_setting.beer_bom_brewery_font_bold_toggle,
        Beerscreen_setting.beer_bom_brewery_font_italic_toggle,
        Beerscreen_setting.beer_bom_brewery_font_underline_toggle,

        Beerscreen_setting.beer_background_color_one,
        Beerscreen_setting.beer_background_color_two,
        Beerscreen_setting.beer_background_color_three,
        Beerscreen_setting.beer_background_color_four,
        Beerscreen_setting.beer_background_color_five,
        Beerscreen_setting.beer_background_color_direction,

        Beerscreen_setting.beer_name_font,
        Beerscreen_setting.beer_name_font_color,
        Beerscreen_setting.beer_name_font_size,
        Beerscreen_setting.beer_name_font_bold_toggle,
        Beerscreen_setting.beer_name_font_italic_toggle,
        Beerscreen_setting.beer_name_font_underline_toggle,

        Beerscreen_setting.beer_style_font,
        Beerscreen_setting.beer_style_font_color,
        Beerscreen_setting.beer_style_font_size,
        Beerscreen_setting.beer_style_font_bold_toggle,
        Beerscreen_setting.beer_style_font_italic_toggle,
        Beerscreen_setting.beer_style_font_underline_toggle,

        Beerscreen_setting.beer_abv_font_color,
        Beerscreen_setting.beer_abv_font_size,
        Beerscreen_setting.beer_abv_font_bold_toggle,
        Beerscreen_setting.beer_abv_font_italic_toggle,
        Beerscreen_setting.beer_abv_font_underline_toggle,

        Beerscreen_setting.beer_ibu_font_color,
        Beerscreen_setting.beer_ibu_font_size,
        Beerscreen_setting.beer_ibu_font_bold_toggle,
        Beerscreen_setting.beer_ibu_font_italic_toggle,
        Beerscreen_setting.beer_ibu_font_underline_toggle,

        Beerscreen_setting.beer_brewery_font,
        Beerscreen_setting.beer_brewery_font_color,
        Beerscreen_setting.beer_brewery_font_size,
        Beerscreen_setting.beer_brewery_font_bold_toggle,
        Beerscreen_setting.beer_brewery_font_italic_toggle,
        Beerscreen_setting.beer_brewery_font_underline_toggle,

        Beerscreen_setting.beer_ticker_bg_color_one,
        Beerscreen_setting.beer_ticker_bg_color_two,
        Beerscreen_setting.beer_ticker_bg_color_three,
        Beerscreen_setting.beer_ticker_bg_color_four,
        Beerscreen_setting.beer_ticker_bg_color_five,
        Beerscreen_setting.beer_ticker_bg_color_direction,
        # font for beer names in the ticker
        Beerscreen_setting.beer_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        Beerscreen_setting.beer_ticker_font,
        Beerscreen_setting.beer_ticker_font_color,
        Beerscreen_setting.beer_ticker_font_size,
        Beerscreen_setting.beer_ticker_font_bold_toggle,
        Beerscreen_setting.beer_ticker_font_italic_toggle,
        Beerscreen_setting.beer_ticker_font_underline_toggle,

        Beerscreen_setting.beer_ticker_toggle,
        Beerscreen_setting.beer_ticker_scroll_speed,

        Beerscreen_setting.venue_db_id,
        Beerscreen_setting.beer_settings_screen_id,
        Beerscreen_setting.beer_screen_template,
        Beerscreen_setting.beer_screen_landscape_portrait_toggle,

        Template.template_name,
        Font_size_option.font_sizes,
    ).join(Template, Beerscreen_setting.beer_screen_template == Template.id
    # ).join(Font_size_option, Beerscreen_setting.beer_bom_name_font_size  == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerBomNameFontSize = db.session.query(
        Beerscreen_setting.beer_bom_name_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_bom_name_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerBomStyleFontSize = db.session.query(
        Beerscreen_setting.beer_bom_style_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_bom_style_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerBomAbvFontSize = db.session.query(
        Beerscreen_setting.beer_bom_abv_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_bom_abv_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerBomIbuFontSize = db.session.query(
        Beerscreen_setting.beer_bom_ibu_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_bom_ibu_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerBomBreweryFontSize = db.session.query(
        Beerscreen_setting.beer_bom_brewery_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_bom_brewery_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerNameFontSize = db.session.query(
        Beerscreen_setting.beer_name_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_name_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerStyleFontSize = db.session.query(
        Beerscreen_setting.beer_style_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_style_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerAbvFontSize = db.session.query(
        Beerscreen_setting.beer_abv_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_abv_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerIbuFontSize = db.session.query(
        Beerscreen_setting.beer_ibu_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_ibu_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerBreweryFontSize = db.session.query(
        Beerscreen_setting.beer_brewery_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_brewery_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    beerTickerFontSize = db.session.query(
        Beerscreen_setting.beer_ticker_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, Beerscreen_setting.beer_ticker_font_size == Font_size_option.id
    ).filter(Beerscreen_setting.beer_settings_screen_id == displayId
    ).filter(Beerscreen_setting.venue_db_id == userId
    ).first()

    this_setting = {
        "fontColorOne" : settings_db.font_color_one,
        "fontColorTwo" : settings_db.font_color_two,
        "fontColorThree" : settings_db.font_color_three,
        "fontColorDirection" : settings_db.font_color_direction,
        "shadowFontColorOne" : settings_db.shadow_font_color_one,
        "shadowFontColorTwo" : settings_db.shadow_font_color_two,
        "shadowFontColorThree" : settings_db.shadow_font_color_three,
        "shadowFontColorDirection" : settings_db.shadow_font_color_direction,

        "screenTemplate" : settings_db.template_name,

        "beerBomBgColorOne" : settings_db.beer_bom_background_color_one,
        "beerBomBgColorTwo" : settings_db.beer_bom_background_color_two,
        "beerBomBgColorThree" : settings_db.beer_bom_background_color_three,
        "beerBomBgColorFour" : settings_db.beer_bom_background_color_four,
        "beerBomBgColorFive" : settings_db.beer_bom_background_color_five,
        "beerBomBgColorDirection" : settings_db.beer_bom_background_color_direction,

        "beerBomNameFont" : settings_db.beer_bom_name_font,
        "beerBomNameFontColor" : settings_db.beer_bom_name_font_color,
        "beerBomNameFontSize" : settings_db.beer_bom_name_font_size,
        "beerBomNameFontSizeDisplay" : beerNameFontSize.font_sizes,
        "beerBomNameFontBoldToggle" : settings_db.beer_bom_name_font_bold_toggle,
        "beerBomNameFontItalicToggle" : settings_db.beer_bom_name_font_italic_toggle,
        "beerBomNameFontUnderlineToggle" : settings_db.beer_bom_name_font_underline_toggle,

        "beerBomStyleFont" : settings_db.beer_bom_style_font,
        "beerBomStyleFontColor" : settings_db.beer_bom_style_font_color,
        "beerBomStyleFontSize" : settings_db.beer_bom_style_font_size,
        "beerBomStyleFontSizeDisplay" : beerBomStyleFontSize.font_sizes,
        "beerBomStyleFontBoldToggle" : settings_db.beer_bom_style_font_bold_toggle,
        "beerBomStyleFontItalicToggle" : settings_db.beer_bom_style_font_italic_toggle,
        "beerBomStyleFontUnderlineToggle" : settings_db.beer_bom_style_font_underline_toggle,

        "beerBomAbvFontColor" : settings_db.beer_bom_abv_font_color,
        "beerBomAbvFontSize" : settings_db.beer_bom_abv_font_size,
        "beerBomAbvFontSizeDisplay" : beerBomAbvFontSize.font_sizes,
        "beerBomAbvFontBoldToggle" : settings_db.beer_bom_abv_font_bold_toggle,
        "beerBomAbvFontItalicToggle" : settings_db.beer_bom_abv_font_italic_toggle,
        "beerBomAbvFontUnderlineToggle" : settings_db.beer_bom_abv_font_underline_toggle,

        "beerBomIbuFontColor" : settings_db.beer_bom_ibu_font_color,
        "beerBomIbuFontSize" : settings_db.beer_bom_ibu_font_size,
        "beerBomIbuFontSizeDisplay" : beerBomIbuFontSize.font_sizes,
        "beerBomIbuFontBoldToggle" : settings_db.beer_bom_ibu_font_bold_toggle,
        "beerBomIbuFontItalicToggle" : settings_db.beer_bom_ibu_font_italic_toggle,
        "beerBomIbuFontUnderlineToggle" : settings_db.beer_bom_ibu_font_underline_toggle,

        "beerBomBreweryFont" : settings_db.beer_bom_brewery_font,
        "beerBomBreweryFontColor" : settings_db.beer_bom_brewery_font_color,
        "beerBomBreweryFontSize" : settings_db.beer_bom_brewery_font_size,
        "beerBomBreweryFontSizeDisplay" : beerBomBreweryFontSize.font_sizes,
        "beerBomBreweryFontBoldToggle" : settings_db.beer_bom_brewery_font_bold_toggle,
        "beerBomBreweryFontItalicToggle" : settings_db.beer_bom_brewery_font_italic_toggle,
        "beerBomBreweryFontUnderlineToggle" : settings_db.beer_bom_brewery_font_underline_toggle,

        "beerBgColorOne" : settings_db.beer_background_color_one,
        "beerBgColorTwo" : settings_db.beer_background_color_two,
        "beerBgColorThree" : settings_db.beer_background_color_three,
        "beerBgColorFour" : settings_db.beer_background_color_four,
        "beerBgColorFive" : settings_db.beer_background_color_five,
        "beerBgColorDirection" : settings_db.beer_background_color_direction,

        "beerNameFont" : settings_db.beer_name_font,
        "beerNameFontColor" : settings_db.beer_name_font_color,
        "beerNameFontSize" : settings_db.beer_name_font_size,
        "beerNameFontSizeDisplay" : beerNameFontSize.font_sizes,
        "beerNameFontBoldToggle" : settings_db.beer_name_font_bold_toggle,
        "beerNameFontItalicToggle" : settings_db.beer_name_font_italic_toggle,
        "beerNameFontUnderlineToggle" : settings_db.beer_name_font_underline_toggle,

        "beerStyleFont" : settings_db.beer_style_font,
        "beerStyleFontColor" : settings_db.beer_style_font_color,
        "beerStyleFontSize" : settings_db.beer_style_font_size,
        "beerStyleFontSizeDisplay" : beerStyleFontSize.font_sizes,
        "beerStyleFontBoldToggle" : settings_db.beer_style_font_bold_toggle,
        "beerStyleFontItalicToggle" : settings_db.beer_style_font_italic_toggle,
        "beerStyleFontUnderlineToggle" : settings_db.beer_style_font_underline_toggle,

        "beerAbvFontColor" : settings_db.beer_abv_font_color,
        "beerAbvFontSize" : settings_db.beer_abv_font_size,
        "beerAbvFontSizeDisplay" : beerAbvFontSize.font_sizes,
        "beerAbvFontBoldToggle" : settings_db.beer_abv_font_bold_toggle,
        "beerAbvFontItalicToggle" : settings_db.beer_abv_font_italic_toggle,
        "beerAbvFontUnderlineToggle" : settings_db.beer_abv_font_underline_toggle,

        "beerIbuFontColor" : settings_db.beer_ibu_font_color,
        "beerIbuFontSize" : settings_db.beer_ibu_font_size,
        "beerIbuFontSizeDisplay" : beerIbuFontSize.font_sizes,
        "beerIbuFontBoldToggle" : settings_db.beer_ibu_font_bold_toggle,
        "beerIbuFontItalicToggle" : settings_db.beer_ibu_font_italic_toggle,
        "beerIbuFontUnderlineToggle" : settings_db.beer_ibu_font_underline_toggle,

        "beerBreweryFont" : settings_db.beer_brewery_font,
        "beerBreweryFontColor" : settings_db.beer_brewery_font_color,
        "beerBreweryFontSize" : settings_db.beer_brewery_font_size,
        "beerBreweryFontSizeDisplay" : beerBreweryFontSize.font_sizes,
        "beerBreweryFontBoldToggle" : settings_db.beer_brewery_font_bold_toggle,
        "beerBreweryFontItalicToggle" : settings_db.beer_brewery_font_italic_toggle,
        "beerBreweryFontUnderlineToggle" : settings_db.beer_brewery_font_underline_toggle,

        "beerTickerBgColorOne" : settings_db.beer_ticker_bg_color_one,
        "beerTickerBgColorTwo" : settings_db.beer_ticker_bg_color_two,
        "beerTickerBgColorThree" : settings_db.beer_ticker_bg_color_three,
        "beerTickerBgColorFour" : settings_db.beer_ticker_bg_color_four,
        "beerTickerBgColorFive" : settings_db.beer_ticker_bg_color_five,
        "beerTickerBgColorDirection" : settings_db.beer_ticker_bg_color_direction,
        # font for beer names in the ticker
        "beerTickerBeernamesFont" : settings_db.beer_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        "beerTickerFont" : settings_db.beer_ticker_font,
        "beerTickerFontColor" : settings_db.beer_ticker_font_color,
        # "beerTickerFontSize" : settings_db.beer_ticker_font_size,
        "beerTickerFontSize" : settings_db.beer_ticker_font_size,
        "beerTickerFontSizeDisplay" : beerTickerFontSize.font_sizes,
        "beerTickerFontBoldToggle" : settings_db.beer_ticker_font_bold_toggle,
        "beerTickerFontItalicToggle" : settings_db.beer_ticker_font_italic_toggle,
        "beerTickerFontUnderlineToggle" : settings_db.beer_ticker_font_underline_toggle,

        "beerTickerToggle" : settings_db.beer_ticker_toggle,
        "beerTickerScrollSpeed" : settings_db.beer_ticker_scroll_speed,

        "beerSettingsScreenId" : settings_db.beer_settings_screen_id,
        "beerscreenTemplate" : settings_db.beer_screen_template,
        "beerscreenLandscapePortraitToggle" : settings_db.beer_screen_landscape_portrait_toggle,
        "venueDbId" : settings_db.venue_db_id,
        "templateName" : settings_db.template_name,
    }
    return this_setting











def _getSettings(current_user_id):
    # settings_db = User_settings.query.filter_by(venue_db_id=current_user.id).first()
    # settings_db = User_settings.query.filter_by(venue_db_id=current_user_id).first()
    settings_db = db.session.query(
        User_settings.number_of_screens,
        User_settings.font_color_one,
        User_settings.font_color_two,
        User_settings.font_color_three,
        User_settings.font_color_direction,
        User_settings.shadow_font_color_one,
        User_settings.shadow_font_color_two,
        User_settings.shadow_font_color_three,
        User_settings.shadow_font_color_direction,

        User_settings.beer_bom_background_color_one,
        User_settings.beer_bom_background_color_two,
        User_settings.beer_bom_background_color_three,
        User_settings.beer_bom_background_color_four,
        User_settings.beer_bom_background_color_five,
        User_settings.beer_bom_background_color_direction,

        User_settings.beer_bom_name_font,
        User_settings.beer_bom_name_font_color,
        User_settings.beer_bom_name_font_size,
        User_settings.beer_bom_name_font_bold_toggle,
        User_settings.beer_bom_name_font_italic_toggle,
        User_settings.beer_bom_name_font_underline_toggle,

        User_settings.beer_bom_style_font,
        User_settings.beer_bom_style_font_color,
        User_settings.beer_bom_style_font_size,
        User_settings.beer_bom_style_font_bold_toggle,
        User_settings.beer_bom_style_font_italic_toggle,
        User_settings.beer_bom_style_font_underline_toggle,

        User_settings.beer_bom_abv_font_color,
        User_settings.beer_bom_abv_font_size,
        User_settings.beer_bom_abv_font_bold_toggle,
        User_settings.beer_bom_abv_font_italic_toggle,
        User_settings.beer_bom_abv_font_underline_toggle,

        User_settings.beer_bom_ibu_font_color,
        User_settings.beer_bom_ibu_font_size,
        User_settings.beer_bom_ibu_font_bold_toggle,
        User_settings.beer_bom_ibu_font_italic_toggle,
        User_settings.beer_bom_ibu_font_underline_toggle,

        User_settings.beer_bom_brewery_font,
        User_settings.beer_bom_brewery_font_color,
        User_settings.beer_bom_brewery_font_size,
        User_settings.beer_bom_brewery_font_bold_toggle,
        User_settings.beer_bom_brewery_font_italic_toggle,
        User_settings.beer_bom_brewery_font_underline_toggle,

        User_settings.beer_background_color_one,
        User_settings.beer_background_color_two,
        User_settings.beer_background_color_three,
        User_settings.beer_background_color_four,
        User_settings.beer_background_color_five,
        User_settings.beer_background_color_direction,

        User_settings.beer_name_font,
        User_settings.beer_name_font_color,
        User_settings.beer_name_font_size,
        User_settings.beer_name_font_bold_toggle,
        User_settings.beer_name_font_italic_toggle,
        User_settings.beer_name_font_underline_toggle,

        User_settings.beer_style_font,
        User_settings.beer_style_font_color,
        User_settings.beer_style_font_size,
        User_settings.beer_style_font_bold_toggle,
        User_settings.beer_style_font_italic_toggle,
        User_settings.beer_style_font_underline_toggle,

        User_settings.beer_abv_font_color,
        User_settings.beer_abv_font_size,
        User_settings.beer_abv_font_bold_toggle,
        User_settings.beer_abv_font_italic_toggle,
        User_settings.beer_abv_font_underline_toggle,

        User_settings.beer_ibu_font_color,
        User_settings.beer_ibu_font_size,
        User_settings.beer_ibu_font_bold_toggle,
        User_settings.beer_ibu_font_italic_toggle,
        User_settings.beer_ibu_font_underline_toggle,

        User_settings.beer_brewery_font,
        User_settings.beer_brewery_font_color,
        User_settings.beer_brewery_font_size,
        User_settings.beer_brewery_font_bold_toggle,
        User_settings.beer_brewery_font_italic_toggle,
        User_settings.beer_brewery_font_underline_toggle,

        User_settings.beer_ticker_bg_color_one,
        User_settings.beer_ticker_bg_color_two,
        User_settings.beer_ticker_bg_color_three,
        User_settings.beer_ticker_bg_color_four,
        User_settings.beer_ticker_bg_color_five,
        User_settings.beer_ticker_bg_color_direction,
        # font for beer names in the ticker
        User_settings.beer_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        User_settings.beer_ticker_font,
        User_settings.beer_ticker_font_color,
        User_settings.beer_ticker_font_size,
        User_settings.beer_ticker_font_bold_toggle,
        User_settings.beer_ticker_font_italic_toggle,
        User_settings.beer_ticker_font_underline_toggle,

        User_settings.beer_ticker_toggle,
        User_settings.beer_ticker_scroll_speed,

        User_settings.wine_name_font,
        User_settings.wine_name_font_color,
        User_settings.wine_name_font_size,
        User_settings.wine_name_font_bold_toggle,
        User_settings.wine_name_font_italic_toggle,
        User_settings.wine_name_font_underline_toggle,

        User_settings.wine_location_font,
        User_settings.wine_location_font_color,
        User_settings.wine_location_font_size,
        User_settings.wine_location_font_bold_toggle,
        User_settings.wine_location_font_italic_toggle,
        User_settings.wine_location_font_underline_toggle,

        User_settings.wine_description_font,
        User_settings.wine_description_font_color,
        User_settings.wine_description_font_size,
        User_settings.wine_description_font_bold_toggle,
        User_settings.wine_description_font_italic_toggle,
        User_settings.wine_description_font_underline_toggle,

        User_settings.wine_glass_font,
        User_settings.wine_glass_font_color,
        User_settings.wine_glass_font_size,
        User_settings.wine_glass_font_bold_toggle,
        User_settings.wine_glass_font_italic_toggle,
        User_settings.wine_glass_font_underline_toggle,

        User_settings.wine_bottle_font,
        User_settings.wine_bottle_font_color,
        User_settings.wine_bottle_font_size,
        User_settings.wine_bottle_font_bold_toggle,
        User_settings.wine_bottle_font_italic_toggle,
        User_settings.wine_bottle_font_underline_toggle,

        User_settings.wine_varietal_font,
        User_settings.wine_varietal_font_color,
        User_settings.wine_varietal_font_size,
        User_settings.wine_varietal_font_bold_toggle,
        User_settings.wine_varietal_font_italic_toggle,
        User_settings.wine_varietal_font_underline_toggle,

        User_settings.wine_type_font,
        User_settings.wine_type_font_color,
        User_settings.wine_type_font_size,
        User_settings.wine_type_font_bold_toggle,
        User_settings.wine_type_font_italic_toggle,
        User_settings.wine_type_font_underline_toggle,

        User_settings.wine_foodPairings_font,
        User_settings.wine_foodPairings_font_color,
        User_settings.wine_foodPairings_font_size,
        User_settings.wine_foodPairings_font_bold_toggle,
        User_settings.wine_foodPairings_font_italic_toggle,
        User_settings.wine_foodPairings_font_underline_toggle,

        User_settings.wine_website_font,
        User_settings.wine_website_font_color,
        User_settings.wine_website_font_size,
        User_settings.wine_website_font_bold_toggle,
        User_settings.wine_website_font_italic_toggle,
        User_settings.wine_website_font_underline_toggle,

        User_settings.wine_ticker_bg_color_one,
        User_settings.wine_ticker_bg_color_two,
        User_settings.wine_ticker_bg_color_three,
        User_settings.wine_ticker_bg_color_four,
        User_settings.wine_ticker_bg_color_five,
        User_settings.wine_ticker_bg_color_direction,
        # font for wine names in the ticker
        User_settings.wine_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        User_settings.wine_ticker_font,
        User_settings.wine_ticker_font_color,
        User_settings.wine_ticker_font_size,
        User_settings.wine_ticker_font_bold_toggle,
        User_settings.wine_ticker_font_italic_toggle,
        User_settings.wine_ticker_font_underline_toggle,

        User_settings.wine_ticker_toggle,
        User_settings.wine_ticker_scroll_speed,

        User_settings.event_name_font,
        User_settings.event_name_font_color,
        User_settings.event_name_font_size,
        User_settings.event_name_font_bold_toggle,
        User_settings.event_name_font_italic_toggle,
        User_settings.event_name_font_underline_toggle,

        User_settings.event_artist_font,
        User_settings.event_artist_font_color,
        User_settings.event_artist_font_size,
        User_settings.event_artist_font_bold_toggle,
        User_settings.event_artist_font_italic_toggle,
        User_settings.event_artist_font_underline_toggle,

        User_settings.event_date_of_event_font,
        User_settings.event_date_of_event_font_color,
        User_settings.event_date_of_event_font_size,
        User_settings.event_date_of_event_font_bold_toggle,
        User_settings.event_date_of_event_font_italic_toggle,
        User_settings.event_date_of_event_font_underline_toggle,

        User_settings.event_starttime_font,
        User_settings.event_starttime_font_color,
        User_settings.event_starttime_font_size,
        User_settings.event_starttime_font_bold_toggle,
        User_settings.event_starttime_font_italic_toggle,
        User_settings.event_starttime_font_underline_toggle,

        User_settings.event_endtime_font,
        User_settings.event_endtime_font_color,
        User_settings.event_endtime_font_size,
        User_settings.event_endtime_font_bold_toggle,
        User_settings.event_endtime_font_italic_toggle,
        User_settings.event_endtime_font_underline_toggle,

        User_settings.event_location_font,
        User_settings.event_location_font_color,
        User_settings.event_location_font_size,
        User_settings.event_location_font_bold_toggle,
        User_settings.event_location_font_italic_toggle,
        User_settings.event_location_font_underline_toggle,

        User_settings.event_ticker_bg_color_one,
        User_settings.event_ticker_bg_color_two,
        User_settings.event_ticker_bg_color_three,
        User_settings.event_ticker_bg_color_four,
        User_settings.event_ticker_bg_color_five,
        User_settings.event_ticker_bg_color_direction,
        # font for event names in the ticker
        User_settings.event_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        User_settings.event_ticker_font,
        User_settings.event_ticker_font_color,
        User_settings.event_ticker_font_size,
        User_settings.event_ticker_font_bold_toggle,
        User_settings.event_ticker_font_italic_toggle,
        User_settings.event_ticker_font_underline_toggle,

        User_settings.event_ticker_toggle,
        User_settings.event_ticker_scroll_speed,

        User_settings.item_name_font,
        User_settings.item_name_font_color,
        User_settings.item_name_font_size,
        User_settings.item_name_font_bold_toggle,
        User_settings.item_name_font_italic_toggle,
        User_settings.item_name_font_underline_toggle,

        User_settings.item_description_font,
        User_settings.item_description_font_color,
        User_settings.item_description_font_size,
        User_settings.item_description_font_bold_toggle,
        User_settings.item_description_font_italic_toggle,
        User_settings.item_description_font_underline_toggle,

        User_settings.item_price_font,
        User_settings.item_price_font_color,
        User_settings.item_price_font_size,
        User_settings.item_price_font_bold_toggle,
        User_settings.item_price_font_italic_toggle,
        User_settings.item_price_font_underline_toggle,

        User_settings.item_ticker_bg_color_one,
        User_settings.item_ticker_bg_color_two,
        User_settings.item_ticker_bg_color_three,
        User_settings.item_ticker_bg_color_four,
        User_settings.item_ticker_bg_color_five,
        User_settings.item_ticker_bg_color_direction,
        # font for item names in the ticker
        User_settings.item_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        User_settings.item_ticker_font,
        User_settings.item_ticker_font_color,
        User_settings.item_ticker_font_size,
        User_settings.item_ticker_font_bold_toggle,
        User_settings.item_ticker_font_italic_toggle,
        User_settings.item_ticker_font_underline_toggle,

        User_settings.item_ticker_toggle,
        User_settings.item_ticker_scroll_speed,

        User_settings.settings_screen_id,
        User_settings.screen_template,
        User_settings.venue_db_id,
        Template.template_name,
        Font_size_option.font_sizes,
    ).join(Template, User_settings.screen_template == Template.id
    ).join(Font_size_option, User_settings.beer_bom_name_font_size  == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    print(settings_db)

    beerBomNameFontSize = db.session.query(
        User_settings.beer_bom_name_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_bom_name_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerBomStyleFontSize = db.session.query(
        User_settings.beer_bom_style_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_bom_style_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerBomAbvFontSize = db.session.query(
        User_settings.beer_bom_abv_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_bom_abv_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerBomIbuFontSize = db.session.query(
        User_settings.beer_bom_ibu_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_bom_ibu_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerBomBreweryFontSize = db.session.query(
        User_settings.beer_bom_brewery_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_bom_brewery_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerNameFontSize = db.session.query(
        User_settings.beer_name_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_name_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerStyleFontSize = db.session.query(
        User_settings.beer_style_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_style_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerAbvFontSize = db.session.query(
        User_settings.beer_abv_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_abv_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerIbuFontSize = db.session.query(
        User_settings.beer_ibu_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_ibu_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerBreweryFontSize = db.session.query(
        User_settings.beer_brewery_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_brewery_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    beerTickerFontSize = db.session.query(
        User_settings.beer_ticker_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.beer_ticker_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()

    wineNameFontSize = db.session.query(
        User_settings.wine_name_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_name_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineLocationFontSize = db.session.query(
        User_settings.wine_location_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_location_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineDescriptionFontSize = db.session.query(
        User_settings.wine_description_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_description_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineGlassFontSize = db.session.query(
        User_settings.wine_glass_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_glass_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineBottleFontSize = db.session.query(
        User_settings.wine_bottle_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_bottle_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineVarietalFontSize = db.session.query(
        User_settings.wine_varietal_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_varietal_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineTypeFontSize = db.session.query(
        User_settings.wine_type_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_type_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineFoodPairingsFontSize = db.session.query(
        User_settings.wine_foodPairings_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_foodPairings_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    wineWebsiteFontSize = db.session.query(
        User_settings.wine_website_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_website_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()



    wineTickerFontSize = db.session.query(
        User_settings.wine_ticker_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.wine_ticker_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    eventNameFontSize = db.session.query(
        User_settings.event_name_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.event_name_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    eventArtistFontSize = db.session.query(
        User_settings.event_artist_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.event_artist_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    eventDateofeventFontSize = db.session.query(
        User_settings.event_date_of_event_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.event_date_of_event_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    eventStarttimeFontSize = db.session.query(
        User_settings.event_starttime_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.event_starttime_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    eventEndtimeFontSize = db.session.query(
        User_settings.event_endtime_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.event_endtime_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    eventLocationFontSize = db.session.query(
        User_settings.event_location_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.event_location_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    eventTickerFontSize = db.session.query(
        User_settings.event_ticker_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.event_ticker_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    itemNameFontSize = db.session.query(
        User_settings.item_name_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.item_name_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    itemDescriptionFontSize = db.session.query(
        User_settings.item_description_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.item_description_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    itemPriceFontSize = db.session.query(
        User_settings.item_price_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.item_price_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()
    itemTickerFontSize = db.session.query(
        User_settings.item_ticker_font_size,
        Font_size_option.font_sizes,
    ).join(Font_size_option, User_settings.item_ticker_font_size == Font_size_option.id
    ).filter(User_settings.venue_db_id == current_user_id
    ).first()


    this_setting = {
        "fontColorOne" : settings_db.font_color_one,
        "fontColorTwo" : settings_db.font_color_two,
        "fontColorThree" : settings_db.font_color_three,
        "fontColorDirection" : settings_db.font_color_direction,
        "shadowFontColorOne" : settings_db.shadow_font_color_one,
        "shadowFontColorTwo" : settings_db.shadow_font_color_two,
        "shadowFontColorThree" : settings_db.shadow_font_color_three,
        "shadowFontColorDirection" : settings_db.shadow_font_color_direction,

        "beerBomBgColorOne" : settings_db.beer_bom_background_color_one,
        "beerBomBgColorTwo" : settings_db.beer_bom_background_color_two,
        "beerBomBgColorThree" : settings_db.beer_bom_background_color_three,
        "beerBomBgColorFour" : settings_db.beer_bom_background_color_four,
        "beerBomBgColorFive" : settings_db.beer_bom_background_color_five,
        "beerBomBgColorDirection" : settings_db.beer_bom_background_color_direction,

        "beerBomNameFont" : settings_db.beer_bom_name_font,
        "beerBomNameFontColor" : settings_db.beer_bom_name_font_color,
        "beerBomNameFontSize" : beerBomNameFontSize.font_sizes,
        "beerBomNameFontBoldToggle" : settings_db.beer_bom_name_font_bold_toggle,
        "beerBomNameFontItalicToggle" : settings_db.beer_bom_name_font_italic_toggle,
        "beerBomNameFontUnderlineToggle" : settings_db.beer_bom_name_font_underline_toggle,

        "beerBomStyleFont" : settings_db.beer_bom_style_font,
        "beerBomStyleFontColor" : settings_db.beer_bom_style_font_color,
        "beerBomStyleFontSize" : beerBomStyleFontSize.font_sizes,
        "beerBomStyleFontBoldToggle" : settings_db.beer_bom_style_font_bold_toggle,
        "beerBomStyleFontItalicToggle" : settings_db.beer_bom_style_font_italic_toggle,
        "beerBomStyleFontUnderlineToggle" : settings_db.beer_bom_style_font_underline_toggle,

        "beerBomAbvFontColor" : settings_db.beer_bom_abv_font_color,
        "beerBomAbvFontSize" : beerBomAbvFontSize.font_sizes,
        "beerBomAbvFontBoldToggle" : settings_db.beer_bom_abv_font_bold_toggle,
        "beerBomAbvFontItalicToggle" : settings_db.beer_bom_abv_font_italic_toggle,
        "beerBomAbvFontUnderlineToggle" : settings_db.beer_bom_abv_font_underline_toggle,

        "beerBomIbuFontColor" : settings_db.beer_bom_ibu_font_color,
        "beerBomIbuFontSize" : beerBomIbuFontSize.font_sizes,
        "beerBomIbuFontBoldToggle" : settings_db.beer_bom_ibu_font_bold_toggle,
        "beerBomIbuFontItalicToggle" : settings_db.beer_bom_ibu_font_italic_toggle,
        "beerBomIbuFontUnderlineToggle" : settings_db.beer_bom_ibu_font_underline_toggle,

        "beerBomBreweryFont" : settings_db.beer_bom_brewery_font,
        "beerBomBreweryFontColof" : settings_db.beer_bom_brewery_font_color,
        "beerBomBreweryFontSize" : beerBomBreweryFontSize.font_sizes,
        "beerBomBreweryFontBoldToggle" : settings_db.beer_bom_brewery_font_bold_toggle,
        "beerBomBreweryFontItalicToggle" : settings_db.beer_bom_brewery_font_italic_toggle,
        "beerBomBreweryFontUnderlineToggle" : settings_db.beer_bom_brewery_font_underline_toggle,

        "beerBgColorOne" : settings_db.beer_background_color_one,
        "beerBgColorTwo" : settings_db.beer_background_color_two,
        "beerBgColorThree" : settings_db.beer_background_color_three,
        "beerBgColorFour" : settings_db.beer_background_color_four,
        "beerBgColorFive" : settings_db.beer_background_color_five,
        "beerBgColorDirection" : settings_db.beer_background_color_direction,

        "beerNameFont" : settings_db.beer_name_font,
        "beerNameFontColor" : settings_db.beer_name_font_color,
        "beerNameFontSize" : beerNameFontSize.font_sizes,
        "beerNameFontBoldToggle" : settings_db.beer_name_font_bold_toggle,
        "beerNameFontItalicToggle" : settings_db.beer_name_font_italic_toggle,
        "beerNameFontUnderlineToggle" : settings_db.beer_name_font_underline_toggle,

        "beerStyleFont" : settings_db.beer_style_font,
        "beerStyleFontColor" : settings_db.beer_style_font_color,
        "beerStyleFontSize" : beerStyleFontSize.font_sizes,
        "beerStyleFontBoldToggle" : settings_db.beer_style_font_bold_toggle,
        "beerStyleFontItalicToggle" : settings_db.beer_style_font_italic_toggle,
        "beerStyleFontUnderlineToggle" : settings_db.beer_style_font_underline_toggle,

        "beerAbvFontColor" : settings_db.beer_abv_font_color,
        "beerAbvFontSize" : beerAbvFontSize.font_sizes,
        "beerAbvFontBoldToggle" : settings_db.beer_abv_font_bold_toggle,
        "beerAbvFontItalicToggle" : settings_db.beer_abv_font_italic_toggle,
        "beerAbvFontUnderlineToggle" : settings_db.beer_abv_font_underline_toggle,

        "beerIbuFontColor" : settings_db.beer_ibu_font_color,
        "beerIbuFontSize" : beerIbuFontSize.font_sizes,
        "beerIbuFontBoldToggle" : settings_db.beer_ibu_font_bold_toggle,
        "beerIbuFontItalicToggle" : settings_db.beer_ibu_font_italic_toggle,
        "beerIbuFontUnderlineToggle" : settings_db.beer_ibu_font_underline_toggle,

        "beerBreweryFont" : settings_db.beer_brewery_font,
        "beerBreweryFontColor" : settings_db.beer_brewery_font_color,
        "beerBreweryFontSize" : beerBreweryFontSize.font_sizes,
        "beerBreweryFontBoldToggle" : settings_db.beer_brewery_font_bold_toggle,
        "beerBreweryFontItalicToggle" : settings_db.beer_brewery_font_italic_toggle,
        "beerBreweryFontUnderlineToggle" : settings_db.beer_brewery_font_underline_toggle,

        "beerTickerBgColorOne" : settings_db.beer_ticker_bg_color_one,
        "beerTickerBgColorTwo" : settings_db.beer_ticker_bg_color_two,
        "beerTickerBgColorThree" : settings_db.beer_ticker_bg_color_three,
        "beerTickerBgColorFour" : settings_db.beer_ticker_bg_color_four,
        "beerTickerBgColorFive" : settings_db.beer_ticker_bg_color_five,
        "beerTickerBgColorDirection" : settings_db.beer_ticker_bg_color_direction,
        # font for beer names in the ticker
        "beerTickerBeernamesFont" : settings_db.beer_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        "beerTickerFont" : settings_db.beer_ticker_font,
        "beerTickerFontColor" : settings_db.beer_ticker_font_color,
        "beerTickerFontSize" : beerTickerFontSize.font_sizes,
        "beerTickerFontBoldToggle" : settings_db.beer_ticker_font_bold_toggle,
        "beerTickerFontItalicToggle" : settings_db.beer_ticker_font_italic_toggle,
        "beerTickerFontUnderlineToggle" : settings_db.beer_ticker_font_underline_toggle,

        "beerTickerToggle" : settings_db.beer_ticker_toggle,
        "beerTickerScrollSpeed" : settings_db.beer_ticker_scroll_speed,

        "wineNameFont" : settings_db.wine_name_font,
        "wineNameFontColor" : settings_db.wine_name_font_color,
        "wineNameFontSize" : wineNameFontSize.font_sizes,
        "wineNameFontBoldToggle" : settings_db.wine_name_font_bold_toggle,
        "wineNameFontItalicToggle" : settings_db.wine_name_font_italic_toggle,
        "wineNameFontUnderlineToggle" : settings_db.wine_name_font_underline_toggle,

        "wineLocationFont" : settings_db.wine_location_font,
        "wineLocationFontColor" : settings_db.wine_location_font_color,
        "wineLocationFontSize" : wineLocationFontSize.font_sizes,
        "wineLocationFontBoldToggle" : settings_db.wine_location_font_bold_toggle,
        "wineLocationFontItalicToggle" : settings_db.wine_location_font_italic_toggle,
        "wineLocationFontUnderlineToggle" : settings_db.wine_location_font_underline_toggle,

        "wineDescriptionFont" : settings_db.wine_description_font,
        "wineDescriptionFontColor" : settings_db.wine_description_font_color,
        "wineDescriptionFontSize" : wineDescriptionFontSize.font_sizes,
        "wineDescriptionFontBoldToggle" : settings_db.wine_description_font_bold_toggle,
        "wineDescriptionFontItalicToggle" : settings_db.wine_description_font_italic_toggle,
        "wineDescriptionFontUnderlineToggle" : settings_db.wine_description_font_underline_toggle,

        "wineGlassFont" : settings_db.wine_glass_font,
        "wineGlassFontColor" : settings_db.wine_glass_font_color,
        "wineGlassFontSize" : wineGlassFontSize.font_sizes,
        "wineGlassFontBoldToggle" : settings_db.wine_glass_font_bold_toggle,
        "wineGlassFontItalicToggle" : settings_db.wine_glass_font_italic_toggle,
        "wineGlassFontUnderlineToggle" : settings_db.wine_glass_font_underline_toggle,

        "wineBottleFont" : settings_db.wine_bottle_font,
        "wineBottleFontColor" : settings_db.wine_bottle_font_color,
        "wineBottleFontSize" : wineBottleFontSize.font_sizes,
        "wineBottleFontBoldToggle" : settings_db.wine_bottle_font_bold_toggle,
        "wineBottleFontItalicToggle" : settings_db.wine_bottle_font_italic_toggle,
        "wineBottleFontUnderlineToggle" : settings_db.wine_bottle_font_underline_toggle,

        "wineVarietalFont" : settings_db.wine_varietal_font,
        "wineVarietalFontColor" : settings_db.wine_varietal_font_color,
        "wineVarietalFontSize" : wineVarietalFontSize.font_sizes,
        "wineVarietalFontBoldToggle" : settings_db.wine_varietal_font_bold_toggle,
        "wineVarietalFontItalicToggle" : settings_db.wine_varietal_font_italic_toggle,
        "wineVarietalFontUnderlineToggle" : settings_db.wine_varietal_font_underline_toggle,

        "wineTypeFont" : settings_db.wine_type_font,
        "wineTypeFontColor" : settings_db.wine_type_font_color,
        "wineTypeFontSize" : wineTypeFontSize.font_sizes,
        "wineTypeFontBoldToggle" : settings_db.wine_type_font_bold_toggle,
        "wineTypeFontItalicToggle" : settings_db.wine_type_font_italic_toggle,
        "wineTypeFontUnderlineToggle" : settings_db.wine_type_font_underline_toggle,

        "wineFoodPairingsFont" : settings_db.wine_foodPairings_font,
        "wineFoodPairingsFontColor" : settings_db.wine_foodPairings_font_color,
        "wineFoodPairingsFontSize" : wineFoodPairingsFontSize.font_sizes,
        "wineFoodPairingsFontBoldToggle" : settings_db.wine_foodPairings_font_bold_toggle,
        "wineFoodPairingsFontItalicToggle" : settings_db.wine_foodPairings_font_italic_toggle,
        "wineFoodpairingsFontUnderlineToggle" : settings_db.wine_foodPairings_font_underline_toggle,

        "wineWebsiteFont" : settings_db.wine_website_font,
        "wineWebsiteFontColor" : settings_db.wine_website_font_color,
        "wineWebsiteFontSize" : wineWebsiteFontSize.font_sizes,
        "wineWebsiteFontBoldToggle" : settings_db.wine_website_font_bold_toggle,
        "wineWebsiteFontItalicToggle" : settings_db.wine_website_font_italic_toggle,
        "wineWebsiteFontUnderlineToggle" : settings_db.wine_website_font_underline_toggle,

        "wineTickerBgColorOne" : settings_db.wine_ticker_bg_color_one,
        "wineTickerBgColorTwo" : settings_db.wine_ticker_bg_color_two,
        "wineTickerBgColorThree" : settings_db.wine_ticker_bg_color_three,
        "wineTickerBgColorFour" : settings_db.wine_ticker_bg_color_four,
        "wineTickerBgColorFive" : settings_db.wine_ticker_bg_color_five,
        "wineTickerBgColorDirection" : settings_db.wine_ticker_bg_color_direction,
        # font for wine names in the ticker
        "wineTickerBeernamesFont" : settings_db.wine_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        "wineTickerFont" : settings_db.wine_ticker_font,
        "wineTickerFontColor" : settings_db.wine_ticker_font_color,
        "wineTickerFontSize" : wineTickerFontSize.font_sizes,
        "wineTickerFontBoldToggle" : settings_db.wine_ticker_font_bold_toggle,
        "wineTickerFontItalicToggle" : settings_db.wine_ticker_font_italic_toggle,
        "wineTickerFontUnderlineToggle" : settings_db.wine_ticker_font_underline_toggle,

        "wineTickerToggle" : settings_db.wine_ticker_toggle,
        "wineTickerScrollSpeed" : settings_db.wine_ticker_scroll_speed,

        "eventNameFont" : settings_db.event_name_font,
        "eventNameFontColor" : settings_db.event_name_font_color,
        "eventNameFontSize" : eventNameFontSize.font_sizes,
        "eventNameFontBoldToggle" : settings_db.event_name_font_bold_toggle,
        "eventNameFontItalicToggle" : settings_db.event_name_font_italic_toggle,
        "eventNameFontUnderlineToggle" : settings_db.event_name_font_underline_toggle,

        "eventArtistFont" : settings_db.event_artist_font,
        "eventArtistFontColor" : settings_db.event_artist_font_color,
        "eventArtistFontSize" : eventArtistFontSize.font_sizes,
        "eventArtistFontBoldToggle" : settings_db.event_artist_font_bold_toggle,
        "eventArtistFontItalicToggle" : settings_db.event_artist_font_italic_toggle,
        "eventArtistFontUnderlineToggle" : settings_db.event_artist_font_underline_toggle,

        "eventDateofeventFont" : settings_db.event_date_of_event_font,
        "eventDateofeventFontColor" : settings_db.event_date_of_event_font_color,
        "eventDateofeventFontSize" : eventDateofeventFontSize.font_sizes,
        "eventDateofeventFontBoldToggle" : settings_db.event_date_of_event_font_bold_toggle,
        "eventDateofeventFontItalicToggle" : settings_db.event_date_of_event_font_italic_toggle,
        "eventDateofeventFontUnderlineToggle" : settings_db.event_date_of_event_font_underline_toggle,

        "eventStarttimeFont" : settings_db.event_starttime_font,
        "eventStarttimeFontColor" : settings_db.event_starttime_font_color,
        "eventStarttimeFontSize" : eventStarttimeFontSize.font_sizes,
        "eventStarttimeFontBoldToggle" : settings_db.event_starttime_font_bold_toggle,
        "eventStarttimeFontItalicToggle" : settings_db.event_starttime_font_italic_toggle,
        "eventStarttimeFontUnderlineToggle" : settings_db.event_starttime_font_underline_toggle,

        "eventEndtimeFont" : settings_db.event_endtime_font,
        "eventEndtimeFontColor" : settings_db.event_endtime_font_color,
        "eventEndtimeFontSize" : eventEndtimeFontSize.font_sizes,
        "eventEndtimeFontBoldToggle" : settings_db.event_endtime_font_bold_toggle,
        "eventEndtimeFontItalicToggle" : settings_db.event_endtime_font_italic_toggle,
        "eventEndtimeFontUnderlineToggle" : settings_db.event_endtime_font_underline_toggle,

        "eventLocationFont" : settings_db.event_location_font,
        "eventLocationFontColor" : settings_db.event_location_font_color,
        "eventLocationFontSize" : eventLocationFontSize.font_sizes,
        "eventLocationFontBoldToggle" : settings_db.event_location_font_bold_toggle,
        "eventLocationFontItalicToggle" : settings_db.event_location_font_italic_toggle,
        "eventLocationFontUnderlineToggle" : settings_db.event_location_font_underline_toggle,

        "eventTickerBgColorOne" : settings_db.event_ticker_bg_color_one,
        "eventTickerBgColorTwo" : settings_db.event_ticker_bg_color_two,
        "eventTickerBgColorThree" : settings_db.event_ticker_bg_color_three,
        "eventTickerBgColorFour" : settings_db.event_ticker_bg_color_four,
        "eventTickerBgColorFive" : settings_db.event_ticker_bg_color_five,
        "eventTickerBgColorDirection" : settings_db.event_ticker_bg_color_direction,
        # font for event names in the ticker
        "eventTickerBeernamesFont" : settings_db.event_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        "eventTickerFont" : settings_db.event_ticker_font,
        "eventTickerFontColor" : settings_db.event_ticker_font_color,
        "eventTickerFontSize" : eventTickerFontSize.font_sizes,
        "eventTickerFontBoldToggle" : settings_db.event_ticker_font_bold_toggle,
        "eventTickerFontItalicToggle" : settings_db.event_ticker_font_italic_toggle,
        "eventTickerFontUnderlineToggle" : settings_db.event_ticker_font_underline_toggle,

        "eventTickerToggle" : settings_db.event_ticker_toggle,
        "eventTickerScrollSpeed" : settings_db.event_ticker_scroll_speed,

        "itemNameFont" : settings_db.item_name_font,
        "itemNameFontColor" : settings_db.item_name_font_color,
        "itemNameFontSize" : itemNameFontSize.font_sizes,
        "itemNameFontBoldToggle" : settings_db.item_name_font_bold_toggle,
        "itemNameFontItalicToggle" : settings_db.item_name_font_italic_toggle,
        "itemNameFontUnderlineToggle" : settings_db.item_name_font_underline_toggle,

        "itemDescriptionFont" : settings_db.item_description_font,
        "itemDescriptionFontColor" : settings_db.item_description_font_color,
        "itemDescriptionFontSize" : itemDescriptionFontSize.font_sizes,
        "itemDescriptionFontBoldToggle" : settings_db.item_description_font_bold_toggle,
        "itemDescriptionFontItalicToggle" : settings_db.item_description_font_italic_toggle,
        "itemDescriptionFontUnderlineToggle" : settings_db.item_description_font_underline_toggle,

        "itemPriceFont" : settings_db.item_price_font,
        "itemPriceFontColor" : settings_db.item_price_font_color,
        "itemPriceFontSize" : itemPriceFontSize.font_sizes,
        "itemPriceFontBoldToggle" : settings_db.item_price_font_bold_toggle,
        "itemPriceFontItalicToggle" : settings_db.item_price_font_italic_toggle,
        "itemPriceFontUnderlineToggle" : settings_db.item_price_font_underline_toggle,

        "itemTickerBgColorOne" : settings_db.item_ticker_bg_color_one,
        "itemTickerBgColorTwo" : settings_db.item_ticker_bg_color_two,
        "itemTickerBgColorThree" : settings_db.item_ticker_bg_color_three,
        "itemTickerBgColorFour" : settings_db.item_ticker_bg_color_four,
        "itemTickerBgColorFive" : settings_db.item_ticker_bg_color_five,
        "itemTickerBgColorDirection" : settings_db.item_ticker_bg_color_direction,
        # font for item names in the ticker
        "itemTickerBeernamesFont" : settings_db.item_ticker_beernames_font,
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        "itemTickerFont" : settings_db.item_ticker_font,
        "itemTickerFontColor" : settings_db.item_ticker_font_color,
        "itemTickerFontSize" : itemTickerFontSize.font_sizes,
        "itemTickerFontBoldToggle" : settings_db.item_ticker_font_bold_toggle,
        "itemTickerFontItalicToggle" : settings_db.item_ticker_font_italic_toggle,
        "itemTickerFontUnderlineToggle" : settings_db.item_ticker_font_underline_toggle,

        "itemTickerToggle" : settings_db.item_ticker_toggle,
        "itemTickerScrollSpeed" : settings_db.item_ticker_scroll_speed,

        "settingsScreenId" : settings_db.settings_screen_id,
        "screenTemplate" : settings_db.screen_template,
        "venueDbId" : settings_db.venue_db_id,
        "templateName" : settings_db.template_name,
    }
    return this_setting
