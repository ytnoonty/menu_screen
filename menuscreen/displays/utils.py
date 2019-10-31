from flask_login import current_user
from menuscreen import db
from menuscreen.models import Ticker

def _getTickerInfo(id):
    thisTicker = Ticker.query.filter(Ticker.venue_db_id == id).first()
    return thisTicker
