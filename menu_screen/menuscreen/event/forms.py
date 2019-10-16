from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DateTimeField, SubmitField, validators
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    eventName = StringField('Event Name:', [validators.Length(min=5, max=100)])
    eventArtist = StringField('Event Artist:', [validators.Length(min=5, max=100)])
    eventDate = DateField('Event Date:', format='%m-%d-%Y')
    eventStartTime = DateTimeField('Event Start Time:', format='%H:%M')
    eventEndTime = DateTimeField('Event End Time:', format='%H:%M')
    eventLocation = StringField('Event Location', [validators.Length(min=5, max=100)])
