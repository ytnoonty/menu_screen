from flask_login import current_user
from menuscreen import db
from menuscreen.models import (User, List_history, List_current, Drink_size, Drink_price,
                                Image_list_history, Image_list_current,
                                Imagescreen_setting, Transition, Wine,
                                Winelist_current, Wine_type, Beerscreen_setting,
                                Winecreen_setting, Eventscreen_setting,
                                Itemscreen_setting, Font_size_option, Template,
                                Event, Item, Ticker, Ticker_type_id)

def getVenueId(name):
    user = User.query.filter_by(venue_name=name).first()
    print(user)
    return user.id

def initListHistory(id):
    list_history = List_history(
        name='TestName',
        style='TestStyle',
        abv='0.0',
        ibu='00',
        brewery='TestBrewery',
        location='TestLocation',
        website='http://www.testwebsite.com',
        description='TestDescription',
        draft_bottle_selection='Draft',
        # beer_logo_image_file='',
        # beer_logo_image_file_id='',
        size_id_1='1',
        price_id_1='1',
        size_id_2='1',
        price_id_2='1',
        size_id_3='1',
        price_id_3='1',
        size_id_4='1',
        price_id_4='1',
        # create_date='',
        venue_db_id=id
    )
    db.session.add(list_history)
    db.session.commit()
    print('********** INIT LIST_CURRENT *********')

def initDrinkSize(id):
    size = Drink_size(
        drink_size_id='1',
        drink_size='-',
        venue_db_id=id
    )
    db.session.add(size)
    db.session.commit()
    print('********** INIT DRINK_SIZES *********')

def initDrinkPrice(id):
    price = Drink_price(
        drink_price_id='1',
        drink_price='-',
        venue_db_id=id
    )
    db.session.add(price)
    db.session.commit()
    print('********** INIT DRINK_PRICES *********')

def initImagelistHistory(id):
    img = Image_list_history(
        logo_image_name="-Test Image-",
        # logo_img_file=,
        venue_db_id=id
    )
    db.session.add(img)
    db.session.commit()
    print('********** INIT IMAGE LIST_HISTORY *********')

def initImagelistCurrent(id):
    img = Image_list_current(
        id_image_history='1',
        id_image_dropdown='1',
        imagescreen_setting_id='1',
        image_screen_id='1',
        venue_db_id=id
    )
    db.session.add(img)
    db.session.commit()
    print('********** INIT IMAGE LIST_CURRENT *********')

def initImagescreenSetting(id):
    settings = Imagescreen_setting(
        img_screen_duration='5',
        transition_id='1',
        venue_db_id=id
    )
    db.session.add(settings)
    db.session.commit()
    print('********** INIT IMAGESCREEN_SETTING *********')

def initTransition(id):
    transition = Transition(
        transition_name='-',
        venue_db_id=id
    )
    db.session.add(transition)
    db.session.commit()
    print('********** INIT TRANSISTION *********')

def initListCurrent(data):
    id = data['id']
    if data['screenId'] == "":
        screenId = 1
    else:
        screenId = data['screenId']
    print('Here is the info: id={}, screenId={}'.format(id, screenId))

    user = User.query.filter_by(id=id).first()
    print('user: {}'.format(user))
    print('id: {}'.format(id))
    beer = List_history.query.filter_by(venue_db_id=id).first()
    print('beer: {}'.format(beer))
    beer_id = beer.id
    print('beer.id: {}'.format(beer.id))

    for x in range(1, 2, 1):
        beer = List_current(id_history=beer_id, id_on_next=beer_id, id_dropdown=x, beer_screen_id=screenId, venue_db_id=id)
        db.session.add(beer)
        db.session.commit()
    print('********** INIT LIST_HISTORY *********')

def initWinelist(id):
    wine = Wine(
        venue_db_id=id,
        name='Wine Name',
        location='Wine Location',
        description = 'Wine Description',
        glass='10',
        bottle = '100',
        varietal='Wine Varietal',
        type='1',
        food_pairings='Wine Food Pairings',
        wine_screen_id='1',
        website='Wine Website'
    )
    db.session.add(wine)
    db.session.commit()

    print('********** INIT WINELIST *********')

def initWinelistCurrent(id):
    wine = Wine.query.filter_by(venue_db_id=id).first()
    print(wine)
    wine_id = wine.id
    for x in range(1, 2, 1):
        wine = Winelist_current(id_wine=wine_id, id_dropdown=x, wine_screen_id='1', venue_db_id=id)
        db.session.add(wine)
        db.session.commit()
    print('********** INIT WINELIST_CURRENT *********')

def initWinetype(id):
    wine = Wine_type(
        type='Type',
        venue_db_id=id
    )
    db.session.add(wine)
    db.session.commit()




def initBeerscreenSetting(data):
    id = data['id']
    if data['screenId'] == "":
        screenId = 1
    else:
        screenId = data['screenId']
    print('Here is the info: id={}, screenId={}'.format(id, screenId))
    beerscreen_settings = Beerscreen_setting(
        font_color_one='#ffffff',
        font_color_two='#ffffff',
        font_color_three='#ffffff',
        font_color_direction='to bottom',
        shadow_font_color_one='#ffffff',
        shadow_font_color_two='#ffffff',
        shadow_font_color_three='#ffffff',
        shadow_font_color_direction='to bottom',

        beer_bom_background_color_one='#ffffff',
        beer_bom_background_color_two='#ffffff',
        beer_bom_background_color_three='#ffffff',
        beer_bom_background_color_four='#ffffff',
        beer_bom_background_color_five='#ffffff',
        beer_bom_background_color_direction='to bottom',

        beer_bom_name_font='1',
        beer_bom_name_font_color='#ffffff',
        beer_bom_name_font_size='1',
        beer_bom_name_font_bold_toggle=0,
        beer_bom_name_font_italic_toggle=0,
        beer_bom_name_font_underline_toggle=0,

        beer_bom_style_font='1',
        beer_bom_style_font_color='#ffffff',
        beer_bom_style_font_size='1',
        beer_bom_style_font_bold_toggle=0,
        beer_bom_style_font_italic_toggle=0,
        beer_bom_style_font_underline_toggle=0,

        beer_bom_abv_font_color='#ffffff',
        beer_bom_abv_font_size='1',
        beer_bom_abv_font_bold_toggle=0,
        beer_bom_abv_font_italic_toggle=0,
        beer_bom_abv_font_underline_toggle=0,

        beer_bom_ibu_font_color='#ffffff',
        beer_bom_ibu_font_size='1',
        beer_bom_ibu_font_bold_toggle=0,
        beer_bom_ibu_font_italic_toggle=0,
        beer_bom_ibu_font_underline_toggle=0,

        beer_bom_brewery_font='1',
        beer_bom_brewery_font_color='#ffffff',
        beer_bom_brewery_font_size='1',
        beer_bom_brewery_font_bold_toggle=0,
        beer_bom_brewery_font_italic_toggle=0,
        beer_bom_brewery_font_underline_toggle=0,

        beer_background_color_one='#000000',
        beer_background_color_two='#000000',
        beer_background_color_three='#000000',
        beer_background_color_four='#000000',
        beer_background_color_five='#000000',
        beer_background_color_direction='to bottom',

        beer_name_font='1',
        beer_name_font_color='#ffffff',
        beer_name_font_size='1',
        beer_name_font_bold_toggle=0,
        beer_name_font_italic_toggle=0,
        beer_name_font_underline_toggle=0,

        beer_style_font='1',
        beer_style_font_color='#ffffff',
        beer_style_font_size='1',
        beer_style_font_bold_toggle=0,
        beer_style_font_italic_toggle=0,
        beer_style_font_underline_toggle=0,

        beer_abv_font_color='#ffffff',
        beer_abv_font_size='1',
        beer_abv_font_bold_toggle=0,
        beer_abv_font_italic_toggle=0,
        beer_abv_font_underline_toggle=0,

        beer_ibu_font_color='#ffffff',
        beer_ibu_font_size='1',
        beer_ibu_font_bold_toggle=0,
        beer_ibu_font_italic_toggle=0,
        beer_ibu_font_underline_toggle=0,

        beer_brewery_font='1',
        beer_brewery_font_color='#ffffff',
        beer_brewery_font_size='1',
        beer_brewery_font_bold_toggle=0,
        beer_brewery_font_italic_toggle=0,
        beer_brewery_font_underline_toggle=0,

        beer_ticker_bg_color_one='#ffffff',
        beer_ticker_bg_color_two='#ffffff',
        beer_ticker_bg_color_three='#ffffff',
        beer_ticker_bg_color_four='#ffffff',
        beer_ticker_bg_color_five='#ffffff',
        beer_ticker_bg_color_direction='to bottom',
        # font for beer names in the ticker
        beer_ticker_beernames_font='1',
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        beer_ticker_font='1',
        beer_ticker_font_color='#ffffff',
        beer_ticker_font_size='1',
        beer_ticker_font_bold_toggle=0,
        beer_ticker_font_italic_toggle=0,
        beer_ticker_font_underline_toggle=0,

        beer_ticker_toggle=0,
        beer_ticker_scroll_speed=10,

        beer_screen_landscape_portrait_toggle=0,
        beer_settings_screen_id =screenId,
        beer_screen_template ='1',
        venue_db_id=id,
    )
    db.session.add(beerscreen_settings)
    db.session.commit()
    print('********** INIT BEERSCREEN SETTINGS *********')

def initWinecreenSetting(id):
    winescreen_settings = Winecreen_setting(
        venue_db_id=id,
        wine_settings_screen_id ='1',
        wine_screen_template ='1',

        wine_name_font='1',
        wine_name_font_color='#ffffff',
        wine_name_font_size='1',
        wine_name_font_bold_toggle=0,
        wine_name_font_italic_toggle=0,
        wine_name_font_underline_toggle=0,

        wine_location_font='1',
        wine_location_font_color='#ffffff',
        wine_location_font_size='1',
        wine_location_font_bold_toggle=0,
        wine_location_font_italic_toggle=0,
        wine_location_font_underline_toggle=0,

        wine_description_font='1',
        wine_description_font_color='#ffffff',
        wine_description_font_size='1',
        wine_description_font_bold_toggle=0,
        wine_description_font_italic_toggle=0,
        wine_description_font_underline_toggle=0,

        wine_glass_font='1',
        wine_glass_font_color='#ffffff',
        wine_glass_font_size='1',
        wine_glass_font_bold_toggle=0,
        wine_glass_font_italic_toggle=0,
        wine_glass_font_underline_toggle=0,

        wine_bottle_font='1',
        wine_bottle_font_color='#ffffff',
        wine_bottle_font_size='1',
        wine_bottle_font_bold_toggle=0,
        wine_bottle_font_italic_toggle=0,
        wine_bottle_font_underline_toggle=0,

        wine_varietal_font='1',
        wine_varietal_font_color='#ffffff',
        wine_varietal_font_size='1',
        wine_varietal_font_bold_toggle=0,
        wine_varietal_font_italic_toggle=0,
        wine_varietal_font_underline_toggle=0,

        wine_type_font='1',
        wine_type_font_color='#ffffff',
        wine_type_font_size='1',
        wine_type_font_bold_toggle=0,
        wine_type_font_italic_toggle=0,
        wine_type_font_underline_toggle=0,

        wine_foodPairings_font='1',
        wine_foodPairings_font_color='#ffffff',
        wine_foodPairings_font_size='1',
        wine_foodPairings_font_bold_toggle=0,
        wine_foodPairings_font_italic_toggle=0,
        wine_foodPairings_font_underline_toggle=0,

        wine_website_font='1',
        wine_website_font_color='#ffffff',
        wine_website_font_size='1',
        wine_website_font_bold_toggle=0,
        wine_website_font_italic_toggle=0,
        wine_website_font_underline_toggle=0,

        wine_ticker_bg_color_one='#ffffff',
        wine_ticker_bg_color_two='#ffffff',
        wine_ticker_bg_color_three='#ffffff',
        wine_ticker_bg_color_four='#ffffff',
        wine_ticker_bg_color_five='#ffffff',
        wine_ticker_bg_color_direction='to bottom',
        # font for Wine names in the ticker
        wine_ticker_beernames_font='1',
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        wine_ticker_font='1',
        wine_ticker_font_color='#ffffff',
        wine_ticker_font_size='1',
        wine_ticker_font_bold_toggle=0,
        wine_ticker_font_italic_toggle=0,
        wine_ticker_font_underline_toggle=0,

        wine_ticker_toggle=0,
        wine_ticker_scroll_speed=10,
    )
    db.session.add(winescreen_settings)
    db.session.commit()
    print('********** INIT WINESCREEN SETTINGS *********')

def initEventscreenSetting(id):
    eventscreen_settings = Eventscreen_setting(
        venue_db_id=id,
        event_settings_screen_id ='1',
        event_screen_template ='1',

        event_name_font='1',
        event_name_font_color='#ffffff',
        event_name_font_size='1',
        event_name_font_bold_toggle=0,
        event_name_font_italic_toggle=0,
        event_name_font_underline_toggle=0,

        event_artist_font='1',
        event_artist_font_color='#ffffff',
        event_artist_font_size='1',
        event_artist_font_bold_toggle=0,
        event_artist_font_italic_toggle=0,
        event_artist_font_underline_toggle=0,

        event_date_of_event_font='1',
        event_date_of_event_font_color='#ffffff',
        event_date_of_event_font_size='1',
        event_date_of_event_font_bold_toggle=0,
        event_date_of_event_font_italic_toggle=0,
        event_date_of_event_font_underline_toggle=0,

        event_starttime_font='1',
        event_starttime_font_color='#ffffff',
        event_starttime_font_size='1',
        event_starttime_font_bold_toggle=0,
        event_starttime_font_italic_toggle=0,
        event_starttime_font_underline_toggle=0,

        event_endtime_font='1',
        event_endtime_font_color='#ffffff',
        event_endtime_font_size='1',
        event_endtime_font_bold_toggle=0,
        event_endtime_font_italic_toggle=0,
        event_endtime_font_underline_toggle=0,

        event_location_font='1',
        event_location_font_color='#ffffff',
        event_location_font_size='1',
        event_location_font_bold_toggle=0,
        event_location_font_italic_toggle=0,
        event_location_font_underline_toggle=0,

        event_ticker_bg_color_one='#ffffff',
        event_ticker_bg_color_two='#ffffff',
        event_ticker_bg_color_three='#ffffff',
        event_ticker_bg_color_four='#ffffff',
        event_ticker_bg_color_five='#ffffff',
        event_ticker_bg_color_direction='to bottom',
        # font for event names in the ticker
        event_ticker_beernames_font='1',
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        event_ticker_font='1',
        event_ticker_font_color='#ffffff',
        event_ticker_font_size='1',
        event_ticker_font_bold_toggle=0,
        event_ticker_font_italic_toggle=0,
        event_ticker_font_underline_toggle=0,

        event_ticker_toggle=0,
        event_ticker_scroll_speed=10,
    )
    db.session.add(eventscreen_settings)
    db.session.commit()
    print('********** INIT EVENTSCREEN SETTINGS *********')

def initItemscreenSetting(id):
    itemscreen_settings = Itemscreen_setting(
        venue_db_id=id,
        item_settings_screen_id ='1',
        item_screen_template ='1',

        item_name_font='1',
        item_name_font_color='#ffffff',
        item_name_font_size='1',
        item_name_font_bold_toggle=0,
        item_name_font_italic_toggle=0,
        item_name_font_underline_toggle=0,

        item_description_font='1',
        item_description_font_color='#ffffff',
        item_description_font_size='1',
        item_description_font_bold_toggle=0,
        item_description_font_italic_toggle=0,
        item_description_font_underline_toggle=0,

        item_price_font='1',
        item_price_font_color='#ffffff',
        item_price_font_size='1',
        item_price_font_bold_toggle=0,
        item_price_font_italic_toggle=0,
        item_price_font_underline_toggle=0,

        item_ticker_bg_color_one='#ffffff',
        item_ticker_bg_color_two='#ffffff',
        item_ticker_bg_color_three='#ffffff',
        item_ticker_bg_color_four='#ffffff',
        item_ticker_bg_color_five='#ffffff',
        item_ticker_bg_color_direction='to bottom',
        # font for item names in the ticker
        item_ticker_beernames_font='1',
        # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
        item_ticker_font='1',
        item_ticker_font_color='#ffffff',
        item_ticker_font_size='1',
        item_ticker_font_bold_toggle=0,
        item_ticker_font_italic_toggle=0,
        item_ticker_font_underline_toggle=0,

        item_ticker_toggle=0,
        item_ticker_scroll_speed=10,
    )
    db.session.add(itemscreen_settings)
    db.session.commit()
    print('********** INIT ITEMSCREEN SETTINGS *********')




def initFontSizeOption(id):
    fontSizes = ["0.5em","0.75em","1.0em","1.25em","1.5em","1.75em","2.0em","2.25em","2.5em","2.75em","3.0em","3.25em","3.5em","3.75em","4.0em","4.25em","4.5em","4.75em","5.0em"]
    for size in fontSizes:
        fontSizeOptions = Font_size_option(
            font_sizes=size,
            venue_db_id=id
        )
        db.session.add(fontSizeOptions)
    db.session.commit()
    print('********** INIT FONT SIZE OPTIONS *********')

def initTemplate(id):
    template = Template(
        template_name='2 Columns, Name, ABV, IBU',
        screen_number='1',
        active_template='disabled',
        template_screen_id='1',
        venue_db_id=id
    )
    db.session.add(template)
    db.session.commit()
    print('********** INIT TEMPLATE *********')

def initEvent(id):
    event = Event(
        name='Event Name',
        artist='Artist',
        location='Event Location',
        event_screen_id='1',
        venue_db_id=id
    )
    db.session.add(event)
    db.session.commit()
    print('********** EVENT TEMPLATE *********')

def initItem(id):
    item = Item(
        name='Test Item Name',
        description='Test Item Description',
        price='Test Item Price',
        item_screen_id='1',
        venue_db_id=id
    )
    db.session.add(item)
    db.session.commit()
    print('********** INIT ITEM *********')

def initTicker(id):
    tickerInfo = Ticker(
        ticker_text='Initialized BEER Ticker Text please add your news and information to show in the scrolling ticker on the display screen.',
        ticker_screen_id='1',
        ticker_type='1',
        venue_db_id=id
    )
    db.session.add(tickerInfo)
    tickerInfo = Ticker(
        ticker_text='Initialized WINE Ticker Text please add your news and information to show in the scrolling ticker on the display screen.',
        ticker_screen_id='1',
        ticker_type='2',
        venue_db_id=id
    )
    db.session.add(tickerInfo)
    tickerInfo = Ticker(
        ticker_text='Initialized EVENT Ticker Text please add your news and information to show in the scrolling ticker on the display screen.',
        ticker_screen_id='1',
        ticker_type='3',
        venue_db_id=id
    )
    db.session.add(tickerInfo)
    tickerInfo = Ticker(
        ticker_text='Initialized ITEM Ticker Text please add your news and information to show in the scrolling ticker on the display screen.',
        ticker_screen_id='1',
        ticker_type='4',
        venue_db_id=id
    )
    db.session.add(tickerInfo)
    db.session.commit()
    print('********** INIT TICKER *********')

def initTickerSingleTicker(data):
    newTickerInfo = Ticker(
        ticker_text='Initialized NEW Ticker Text please add your news and information to show in the scrolling ticker on the display screen.',
        ticker_screen_id=data['screenId'],
        ticker_type=data['tickerTypeId'],
        venue_db_id=data['id'],
    )
    db.session.add(newTickerInfo)
    db.session.commit()
    print('********** INIT SINGLE TICKER WITH SPECIFIC TICKER TYPE FOR A NEW DISPLAY SCREEN*******')

def initTickerTypeId(id):
    tickerTypeCandidate = Ticker_type_id(
        ticker_type='Beer',
        ticker_type_id_fk='1',
        venue_db_id=id
    )
    db.session.add(tickerTypeCandidate)
    tickerTypeCandidate = Ticker_type_id(
        ticker_type='Wine',
        ticker_type_id_fk='2',
        venue_db_id=id
    )
    db.session.add(tickerTypeCandidate)
    tickerTypeCandidate = Ticker_type_id(
        ticker_type='Event',
        ticker_type_id_fk='3',
        venue_db_id=id
    )
    db.session.add(tickerTypeCandidate)
    tickerTypeCandidate = Ticker_type_id(
        ticker_type='Item',
        ticker_type_id_fk='4',
        venue_db_id=id
    )
    db.session.add(tickerTypeCandidate)
    db.session.commit()
    print('********** INIT TICKER TYPE ID ***********')
