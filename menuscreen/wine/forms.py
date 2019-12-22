from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired

# Wine Form Class
class WineForm(FlaskForm):
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=1, max=100)
    ])
    location = StringField('Location', [
        validators.DataRequired(),
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
        validators.DataRequired(),
        validators.Length(min=1)
    ])

    type = SelectField(u'Type', [
        validators.optional()
    ], coerce=int, option_widget=None)

    food_pairings = TextAreaField('Food Pairings', [
        validators.optional()
    ])
    website = StringField('Website', [
        validators.optional(),
        validators.length(max=100)
    ])

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


# Wine type form class
class WineTypeForm(FlaskForm):
    wineType = StringField('Type of Wine', [
        validators.Length(min=1, max=50)
    ])
    wineTypeSelect = SelectField(u'Types', [
        validators.optional()
    ], option_widget=None)
