from flask_login import current_user
from menuscreen import db
from menuscreen.models import Ticker, Ticker_type_id, Beerscreen_settings

def _getTickerInfo(screenData):
    print("screenData: {}".format(screenData))
    userId = screenData['userId']
    screenNumber = screenData['screenNumber']
    ticker = db.session.query(
        Ticker.id,
        Ticker.ticker_text,
        Ticker.ticker_screen_id,
        Ticker_type_id.ticker_type,
    ).join(Ticker_type_id, Ticker_type_id.ticker_type_id_fk == Ticker.ticker_type
    ).filter(Ticker.ticker_screen_id == screenNumber
    ).filter(Ticker.venue_db_id == userId
    ).first()
    return ticker

def _getNumberOfBeerScreens(id):
    print("id: {}".format(id))
    numberOfScreens = db.session.query(
        Beerscreen_settings.beer_settings_screen_id,
    ).filter(Beerscreen_settings.venue_db_id == id
    ).all()
    return numberOfScreens
