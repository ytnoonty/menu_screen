from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, IntegerField, BooleanField, validators
from wtforms.validators import DataRequired

class SettingsForm(FlaskForm):
    numberOfScreens = SelectField(u'Number Of Screens', coerce=int, option_widget=None)
    beerscreenSettingsId = SelectField(u'Beerscreen Number', coerce=int, option_widget=None)
    fontColorOne = StringField('Font Color Code One:')
    fontColorTwo = StringField('Font Color Code Two')
    fontColorThree = StringField('Font Color Code Three')
    fontColorDirection = SelectField('Font Color Direction')
    shadowFontColorOne = StringField('Shadow Font Color Code One:')
    shadowFontColorTwo = StringField('Shadow Font Color Code Two')
    shadowFontColorThree = StringField('Shadow Font Color Code Three')
    shadowFontColorDirection = SelectField('Shadow Font Color Direction')
    backgroundColorOne = StringField('Background Font Color Code One:')
    backgroundColorTwo = StringField('Background Font Color Code Two')
    backgroundColorThree = StringField('Background Font Color Code Three')
    backgroundColorDirection = SelectField('Background Font Color Direction')
    nameFontColor = StringField('Name Font Color Code:')
    styleFontColor = StringField('Style Font Color Code:')
    abvFontColor = StringField('ABV Font Color Code:')
    ibuFontColor = StringField('IBU Font Color Code:')
    breweryFontColor = StringField('Brewery Font Color Code:')
    nameFontSize = SelectField(u'Name Font Size', coerce=int, option_widget=None)
    styleFontSize = SelectField(u'Style Font Size', coerce=int, option_widget=None)
    abvFontSize = SelectField(u'ABV Font Size', coerce=int, option_widget=None)
    ibuFontSize = SelectField(u'IBU Font Size', coerce=int, option_widget=None)
    breweryFontSize =  SelectField(u'Brewery Font Size', coerce=int, option_widget=None)
    screenTemplate = SelectField(u'Screen Template', [validators.optional()], coerce=int, option_widget=None)
    tickerToggle = BooleanField(u'Show Ticker:', default=False)
    tickerScrollSpeed = IntegerField(u'Ticker Scroll Speed', [
        validators.DataRequired()
    ])

class FontSizeForm(FlaskForm):
    fontSizeOptions = DecimalField('Font Size Options (Min: 0.0 - Max: 5.0)', [validators.DataRequired(), validators.NumberRange(min=0, max=5.0)])
    fontSizes = SelectField(u'Font Sizes', [validators.optional()], coerce=int, option_widget=None)
class TemplateForm(FlaskForm):
    templateName = StringField('Name of Screen Template', [validators.Length(min=1, max=50)])
    templateSelect = SelectField(u'Templates', [validators.optional()], option_widget=None)
