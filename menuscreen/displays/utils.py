from flask_login import current_user
from menuscreen import db
from menuscreen.models import Ticker

def _getTickerInfo(user_id):
    print("user_id: {}".format(user_id))
    ticker = db.session.query(
    Ticker.id,
    Ticker.ticker_text,
    Ticker.tickerscreen_id,
    ).filter(Ticker.venue_db_id == user_id
    ).first()
    print("ticker: {}".format(ticker))
    return ticker
