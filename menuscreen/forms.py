# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
# from flask_login import current_user
# from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, RadioField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField, validators
# from wtforms.validators import DataRequired, Length, ValidationError
# from menuscreen.models import User






class SettingsForm(FlaskForm):
    fontColor = StringField('Font Color Code:')
    backgroundColor = StringField('Background Color Code:')
    nameFontSize = SelectField(u'Name Font Size', coerce=int, option_widget=None)
    abvIbuFontSize = SelectField(u'Abv, Ibu, Font Size', coerce=int, option_widget=None)
    screenTemplate = SelectField(u'Screen Template', [
        validators.optional()
    ], coerce=int, option_widget=None)

class FontSizeForm(FlaskForm):
    fontSizeOptions = DecimalField('Font Size Options (Min: 0.0 - Max: 5.0)', [
        validators.DataRequired(),
        validators.NumberRange(min=0, max=5.0)
    ])
    fontSizes = SelectField(u'Font Sizes', [
        validators.optional()
    ], coerce=int, option_widget=None)

class TemplateForm(FlaskForm):
    templateName = StringField('Name of Screen Template', [
        validators.Length(min=1, max=50)
    ])
    templateSelect = SelectField(u'Templates', [
        validators.optional()
    ], option_widget=None)

# Wine Form Class
class WineForm(FlaskForm):
    name = StringField('Name', [
        validators.required(),
        validators.Length(min=1, max=100)
    ])
    location = StringField('Location', [
        validators.required(),
        validators.Length(min=1, max=100)
    ])
    glass = StringField('Glass', [
        validators.optional(),
        validators.Length(min=0)
    ])
    bottle = StringField('Bottle', [
        validators.optional(),
        validators.Length(min=0)
    ])
    description = TextAreaField('Description', [
        validators.optional(),
        validators.length(min=1)
    ])
    varietal = StringField('Varietal', [
    validators.required(),
    validators.Length(min=1)
    ])

    type = SelectField(u'Type', coerce=int, option_widget=None)

    foodPairings = TextAreaField('Food Pairings', [
        validators.optional()
    ])
    website = StringField('Website', [
        validators.optional(),
        validators.length(max=100)
    ])

class EventForm(FlaskForm):
    eventName = StringField('Event Name:', [
        validators.Length(min=5, max=100)
    ])
    eventArtist = StringField('Event Artist:', [
        validators.Length(min=5, max=100)
    ])
    eventDate = DateField('Event Date:', format='%m-%d-%Y')
    eventTime = DateTimeField('Event Time:', format='%H:%M:%S')
    eventEndTime = DateTimeField('Event End Time:', format='%H:%M:%S')
    eventLocation = StringField('Event Location', [
        validators.Length(min=5, max=100)
    ])


# Class for the beer list
class CurrentBeerListForm(FlaskForm):
    beer1 = SelectField(u'Beer 1', coerce=int, option_widget=None)
    beer2 = SelectField(u'Beer 2', coerce=int, option_widget=None)
    beer3 = SelectField(u'Beer 3', coerce=int, option_widget=None)
    beer4 = SelectField(u'Beer 4', coerce=int, option_widget=None)
    beer5 = SelectField(u'Beer 5', coerce=int, option_widget=None)
    beer6 = SelectField(u'Beer 6', coerce=int, option_widget=None)
    beer7 = SelectField(u'Beer 7', coerce=int, option_widget=None)
    beer8 = SelectField(u'Beer 8', coerce=int, option_widget=None)
    beer9 = SelectField(u'Beer 9', coerce=int, option_widget=None)
    beer10 = SelectField(u'Beer 10', coerce=int, option_widget=None)
    beer11 = SelectField(u'Beer 11', coerce=int, option_widget=None)
    beer12 = SelectField(u'Beer 12', coerce=int, option_widget=None)
    beer13 = SelectField(u'Beer 13', coerce=int, option_widget=None)
    beer14 = SelectField(u'Beer 14', coerce=int, option_widget=None)
    beer15 = SelectField(u'Beer 15', coerce=int, option_widget=None)
    beer16 = SelectField(u'Beer 16', coerce=int, option_widget=None)
    beer17 = SelectField(u'Beer 17', coerce=int, option_widget=None)
    beer18 = SelectField(u'Beer 18', coerce=int, option_widget=None)
    beer19 = SelectField(u'Beer 19', coerce=int, option_widget=None)
    beer20 = SelectField(u'Beer 20', coerce=int, option_widget=None)
    beer21 = SelectField(u'Beer 21', coerce=int, option_widget=None)
    #tickerHeadline
    beer22 = SelectField(u'Ticker Headline', coerce=int, option_widget=None)

# Class for the beer list
class NextBeerListForm(FlaskForm):
    beer1 = SelectField(u'Beer 1', coerce=int, option_widget=None)
    beer2 = SelectField(u'Beer 2', coerce=int, option_widget=None)
    beer3 = SelectField(u'Beer 3', coerce=int, option_widget=None)
    beer4 = SelectField(u'Beer 4', coerce=int, option_widget=None)
    beer5 = SelectField(u'Beer 5', coerce=int, option_widget=None)
    beer6 = SelectField(u'Beer 6', coerce=int, option_widget=None)
    beer7 = SelectField(u'Beer 7', coerce=int, option_widget=None)
    beer8 = SelectField(u'Beer 8', coerce=int, option_widget=None)
    beer9 = SelectField(u'Beer 9', coerce=int, option_widget=None)
    beer10 = SelectField(u'Beer 10', coerce=int, option_widget=None)
    beer11 = SelectField(u'Beer 11', coerce=int, option_widget=None)
    beer12 = SelectField(u'Beer 12', coerce=int, option_widget=None)
    beer13 = SelectField(u'Beer 13', coerce=int, option_widget=None)
    beer14 = SelectField(u'Beer 14', coerce=int, option_widget=None)
    beer15 = SelectField(u'Beer 15', coerce=int, option_widget=None)
    beer16 = SelectField(u'Beer 16', coerce=int, option_widget=None)

# Class for winelist
class CurrentWinelistForm(FlaskForm):
    winenum1 = '1'
    wine1 = SelectField(u'Wine ' + winenum1, coerce=int, option_widget=None)
    wine2 = SelectField(u'Wine 2', coerce=int, option_widget=None)
    wine3 = SelectField(u'Wine 3', coerce=int, option_widget=None)
    wine4 = SelectField(u'Wine 4', coerce=int, option_widget=None)
    wine5 = SelectField(u'Wine 5', coerce=int, option_widget=None)
    wine6 = SelectField(u'Wine 6', coerce=int, option_widget=None)
    wine7 = SelectField(u'Wine 7', coerce=int, option_widget=None)
    wine8 = SelectField(u'Wine 8', coerce=int, option_widget=None)
    wine9 = SelectField(u'Wine 9', coerce=int, option_widget=None)
    wine10 = SelectField(u'Wine 10', coerce=int, option_widget=None)
    wine11 = SelectField(u'Wine 11', coerce=int, option_widget=None)
    wine12 = SelectField(u'Wine 12', coerce=int, option_widget=None)
    wine13 = SelectField(u'Wine 13', coerce=int, option_widget=None)
    wine14 = SelectField(u'Wine 14', coerce=int, option_widget=None)
    wine15 = SelectField(u'Wine 15', coerce=int, option_widget=None)
    wine16 = SelectField(u'Wine 16', coerce=int, option_widget=None)
    wine17 = SelectField(u'Wine 17', coerce=int, option_widget=None)
    wine18 = SelectField(u'Wine 18', coerce=int, option_widget=None)
    wine19 = SelectField(u'Wine 19', coerce=int, option_widget=None)
    wine20 = SelectField(u'Wine 20', coerce=int, option_widget=None)
    wine21 = SelectField(u'Wine 21', coerce=int, option_widget=None)
    wine22 = SelectField(u'Wine 22', coerce=int, option_widget=None)
    wine23 = SelectField(u'Wine 23', coerce=int, option_widget=None)
    wine24 = SelectField(u'Wine 24', coerce=int, option_widget=None)
    wine25 = SelectField(u'Wine 25', coerce=int, option_widget=None)
    wine26 = SelectField(u'Wine 26', coerce=int, option_widget=None)
    wine27 = SelectField(u'Wine 27', coerce=int, option_widget=None)
    wine28 = SelectField(u'Wine 28', coerce=int, option_widget=None)
