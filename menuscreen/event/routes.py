from flask import(render_template, url_for, flash, redirect,
                    request, abort, jsonify, Blueprint)
from datetime import datetime
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import User, Event
from menuscreen.event.forms import EventForm
from menuscreen.event.utils import getTime, _getEvents, _getEventsSortAsc
from menuscreen.users.init_db_tables import getVenueId

event = Blueprint('event', __name__)


@event.route('/_get_event_current_list', methods=['GET', 'POST'])
# @login_required
def _get_event_current_list():
    data = request.get_json()
    print("**************************************")
    print("**************************************")
    print("list_history. /_get_event_current_list")
    print(data)
    if (data):
        current_user_id = getVenueId(data['userName'])
        print("DATA HERE")
        print(data['userName'])
        print(current_user_id)
        data = _getEventsSortAsc(current_user_id)
    else:
        print("NO DATA HERE")
        print(current_user.id)
        data = _getEventsSortAsc(current_user.id)
    print("**************************************")
    print("**************************************")
    return jsonify(data)

@event.route('/event_dashboard', methods=['GET', 'POST'])
@login_required
def event_dashboard():
    events = [
        {
            "id":1,
            "artist":"eventArtist",
            "name":"eventName",
            "date_of_event":"eventDOE",
            "starttime_of_event":"eventSTOE",
            "endtime_of_event":"eventETOE",
            "location":"eventLocation",
        }
    ]
    events = _getEvents(current_user.id)
    # events = Event.query.filter_by(venue_db_id=current_user.id).all()
    return render_template('event_dashboard.html', title="Event Dashboard", legend='Event Dashboard', events=events)

@event.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    form = EventForm(request.form)
    if request.method == 'POST':
        event = {
            "eventName":request.form['eventname'],
            "eventArtist":request.form['eventartist'],
            "eventDate":request.form['eventdate'],
            "eventStartTime":request.form['eventstarttime'],
            "eventEndTime":request.form['eventendtime'],
            "eventLocation":request.form['eventlocation'],
        }
        event = Event(
            name=event['eventName'],
            artist=event['eventArtist'],
            date_of_event=event['eventDate'],
            starttime_of_event=event['eventStartTime'],
            endtime_of_event=event['eventEndTime'],
            location=event['eventLocation'],
            venue_db_id=current_user.id
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created', 'success')
        return redirect(url_for('event.event_dashboard'))
    return render_template('add_event.html', title="Add Event", legend='Add Event', form=form)

@event.route('/edit_event/<string:id>', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    # event = Event.query.filter_by(id=id, venue_db_id=current_user.id).first()
    event = Event.query.get_or_404(id)
    if event.venue_db_id != current_user.id:
        abort(403)# Get form
    form = EventForm(request.form)
    # Populate event form fields
    form.eventName.data = event.name
    form.eventArtist.data = event.artist
    form.eventDate.data = event.date_of_event
    form.eventStartTime.data = getTime(event.starttime_of_event)
    form.eventEndTime.data = getTime(event.endtime_of_event)
    form.eventLocation.data = event.location
    print('event: {}'.format(event))

    if request.method == 'POST':
        newEvent = {
            "name" : request.form['eventname'],
            "artist" : request.form['eventartist'],
            "date" : request.form['eventdate'],
            "startTime" : request.form['eventstarttime'],
            "endTime" : request.form['eventendtime'],
            "location" : request.form['eventlocation'],
        }
        event.name = newEvent['name']
        event.artist = newEvent['artist']
        event.date_of_event =  newEvent['date']
        event.starttime_of_event =  newEvent['startTime']
        event.endtime_of_event =  newEvent['endTime']
        event.location =  newEvent['location']
        db.session.commit()
        flash('Event changed!', 'success')
        return redirect(url_for('event.event_dashboard'))
    return render_template('edit_event.html', title="Edit Event", legend='Edit Event', form=form, event=event)

@event.route('/delete_event/<string:id>', methods=['POST'])
@login_required
def delete_event(id):
    # event = Event.query.filter_by(id=id, venue_db_id=current_user.id).first()
    event = Event.query.get_or_404(id)
    if event.venue_db_id != current_user.id:
        abort(403)
    db.session.delete(event)
    db.session.commit()
    flash('Event Deleted!', 'success')
    return redirect(url_for('event.event_dashboard'))
