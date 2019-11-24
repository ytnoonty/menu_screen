from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import User, Event

def getTime(time):
    time = str(time)
    time = time.split(":")
    hour = time[0]
    if int(hour) < 10:
        hour = "" + str(hour)
    min = time[1]
    # sec = time[2]
    time = hour + ':' + min
    # print('time: {}'.format(time))
    return time

def _getEvents(user_id):
    events = Event.query.filter_by(venue_db_id=user_id).all()
    return events

def _getEventsSortAsc(screenData):
    print("screenData: {}".format(screenData))
    userId = screenData['userId']
    displayId = screenData['screenNumber']

    user = User.query.filter_by(id=userId).first()
    eventsDb = user.event_sort_asc
    eventsDb = db.session.query(
        Event.id,
        Event.name,
        Event.artist,
        Event.date_of_event,
        Event.starttime_of_event,
        Event.endtime_of_event,
        Event.location,
        Event.event_screen_id,
        Event.venue_db_id,
    ).filter(Event.event_screen_id == displayId
    ).filter(Event.venue_db_id == userId
    ).order_by(Event.date_of_event
    ).order_by(Event.starttime_of_event
    ).all()
    events = []
    for event in eventsDb:
        event = {
            "id" : event.id,
            "name" : event.name,
            "artist" : event.artist,
            "date_of_event ": str(event.date_of_event),
            "starttime_of_event" : str(event.starttime_of_event),
            "endtime_of_event" : str(event.endtime_of_event),
            "location" : event.location,
            "venue_db_id" : event.venue_db_id,
        }
        events.append(event)
    return events
