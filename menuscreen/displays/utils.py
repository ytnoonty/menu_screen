from flask_login import current_user
from menuscreen import db
from menuscreen.models import Ticker, Ticker_type_id

def _getTickerInfo(screenData):
    print("screenData: {}".format(screenData))
    userId = screenData['userId']
    displayId = screenData['screenNumber']
    ticker = db.session.query(
        Ticker.id,
        Ticker.ticker_text,
        Ticker.ticker_screen_id,
        Ticker_type_id.ticker_type,
    ).join(Ticker_type_id, Ticker_type_id.ticker_type_id_fk == Ticker.ticker_type
    ).filter(Ticker.ticker_screen_id == displayId
    ).filter(Ticker.venue_db_id == userId
    ).first()
    return ticker
