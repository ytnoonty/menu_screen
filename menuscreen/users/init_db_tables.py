from flask_login import current_user
from menuscreen import db
from menuscreen.models import (User, List_history, List_current, Wines,
                                Winelist_current, Wine_type, User_settings,
                                Font_size_options, Template, Event, Item, Ticker)

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
        website='TestWebsite',
        description='TestDescription',
        draft_bottle_selection='Draft',
        # create_date='',
        venue_db_id=id
    )
    db.session.add(list_history)
    db.session.commit()
    print('********** INIT LIST_CURRENT *********')

def initListCurrent(id):
    user = User.query.filter_by(id=id).first()
    print('user: {}'.format(user))
    print('id: {}'.format(id))
    beer = List_history.query.filter_by(venue_db_id=id).first()
    print('beer: {}'.format(beer))
    beer_id = beer.id
    print('beer.id: {}'.format(beer.id))

    for x in range(1, 2, 1):
        beer = List_current(id_history=beer_id, id_on_next=beer_id, id_dropdown=x, beerscreen_id=1, venue_db_id=id)
        db.session.add(beer)
        db.session.commit()
    print('********** INIT LIST_HISTORY *********')

def initWinelist(id):
    wine = Wines(
        venue_db_id=id,
        name='Wine Name',
        location='Wine Location',
        description = 'Wine Description',
        glass='Glass $$',
        bottle = 'Bottle $$',
        varietal='Wine Varietal',
        type='1',
        foodPairings='Wine Food Pairings',
        winescreen_id='1',
        website='Wine Website'
    )
    db.session.add(wine)
    db.session.commit()

    print('********** INIT WINELIST *********')

def initWinelistCurrent(id):
    wine = Wines.query.filter_by(venue_db_id=id).first()
    print(wine)
    wine_id = wine.id
    for x in range(1, 2, 1):
        wine = Winelist_current(id_wine=wine_id, id_dropdown=x, winescreen_id='1', venue_db_id=id)
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

def initUserSettings(id):
    user_setting = User_settings(
    number_of_screens='1',
    beerscreen_settings_id='1',
    font_color_one='#000000',
    font_color_two='#000000',
    font_color_three='#000000',
    font_color_direction='to bottom',
    shadow_font_color_one='#000000',
    shadow_font_color_two='#000000',
    shadow_font_color_three='#000000',
    shadow_font_color_direction='to bottom',
    background_color_one='#000000',
    background_color_two='#000000',
    background_color_three='#000000',
    background_color_direction='to bottom',
    name_font_color='#000000',
    style_font_color='#000000',
    abv_font_color='#000000',
    ibu_font_color='#000000',
    brewery_font_color='#000000',
    name_font_size='1',
    style_font_size='1',
    abv_font_size='1',
    ibu_font_size='1',
    brewery_font_size='1',
    screen_template='1',
    ticker_toggle=0,
    ticker_scroll_speed=10,
    venue_db_id=id
    )
    db.session.add(user_setting)
    db.session.commit()
    print('********** INIT USER SETTINGS *********')

def initFontSizeOptions(id):
    fontSizeOptions = Font_size_options(
        font_sizes='1.0em',
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
        eventscreen_id='1',
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
        itemscreen_id='1',
        venue_db_id=id
    )
    db.session.add(item)
    db.session.commit()
    print('********** INIT ITEM *********')

def initTicker(id):
    tickerInfo = Ticker(
        ticker_text='Test Ticker Text',
        tickerscreen_id='1',
        venue_db_id=id
    )
    db.session.add(tickerInfo)
    db.session.commit()
    print('********** INIT TICKER *********')
