from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, DecimalField, IntegerField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired

class BeerscreenSettingsForm(FlaskForm):
    beerSettingsScreenId = SelectField(u'Screen Id:', coerce=int, option_widget=None)
    beerscreenTemplate = SelectField(u'Screen Template:', [validators.optional()], coerce=int, option_widget=None)

    beerscreenLandscapePortraitToggle = BooleanField(u'Portrait:', default=False)

    fontColorOne = StringField('Font Color Code #1:')
    fontColorTwo = StringField('Font Color Code #2:')
    fontColorThree = StringField('Font Color Code #3:')
    fontColorDirection = SelectField('Font Color Direction:')
    shadowFontColorOne = StringField('Shadow Color Code #1:')
    shadowFontColorTwo = StringField('Shadow Color Code #2:')
    shadowFontColorThree = StringField('Shadow Color Code #3:')
    shadowFontColorDirection = SelectField('Shadow Color Direction:')

    beerBomBgColorOne = StringField('Beer of the Month Background Color Code #1:')
    beerBomBgColorTwo = StringField('Beer of the Month Background Color Code #2:')
    beerBomBgColorThree = StringField('Beer of the Month Background Color Code #3:')
    beerBomBgColorFour = StringField('Beer of the Month Background Color Code #4:')
    beerBomBgColorFive = StringField('Beer of the Month Background Color Code #5:')
    beerBomBgColorDirection = SelectField(u'Beer of the Month Background Color Direction:', option_widget=None)

    beerBomNameFont = SelectField(u'Beer of the Month Name Font:', coerce=int, option_widget=None)
    beerBomNameFontColor = StringField('Beer of the Month Name Font Color Code:')
    beerBomNameFontSize = SelectField(u'Beer of the Month Name Font Size:', coerce=int, option_widget=None)
    beerBomNameFontBoldToggle = BooleanField(u'Beer of the Month Name Bold:', default=False)
    beerBomNameFontItalicToggle = BooleanField(u'Beer of the Month Name Italic:', default=False)
    beerBomNameFontUnderlineToggle = BooleanField(u'Beer of the Month Name Underline:', default=False)

    beerBomStyleFont = SelectField(u'Beer of the Month Style Font:', coerce=int, option_widget=None)
    beerBomStyleFontColor = StringField('Beer of the Month Style Font Color Code:')
    beerBomStyleFontSize = SelectField(u'Beer of the Month Style Font Size:', coerce=int, option_widget=None)
    beerBomStyleFontBoldToggle = BooleanField(u'Beer of the Month Style Bold:', default=False)
    beerBomStyleFontItalicToggle = BooleanField(u'Beer of the Month Style Italic:', default=False)
    beerBomStyleFontUnderlineToggle = BooleanField(u'Beer of the Month Style Underline:', default=False)

    beerBomAbvFontColor = StringField('Beer of the Month Abv Font Color Code:')
    beerBomAbvFontSize = SelectField(u'Beer of the Month Abv Font Size:', coerce=int, option_widget=None)
    beerBomAbvFontBoldToggle = BooleanField(u'Beer of the Month Abv Bold:', default=False)
    beerBomAbvFontItalicToggle = BooleanField(u'Beer of the Month Abv Italic:', default=False)
    beerBomAbvFontUnderlineToggle = BooleanField(u'Beer of the Month Abv Underline:', default=False)

    beerBomIbuFontColor = StringField('Beer of the Month Ibu Font Color Code:')
    beerBomIbuFontSize = SelectField(u'Beer of the Month Ibu Font Size:', coerce=int, option_widget=None)
    beerBomIbuFontBoldToggle = BooleanField(u'Beer of the Month Ibu Bold:', default=False)
    beerBomIbuFontItalicToggle = BooleanField(u'Beer of the Month Ibu Italic:', default=False)
    beerBomIbuFontUnderlineToggle = BooleanField(u'Beer of the Month Ibu Underline:', default=False)

    beerBomBreweryFont = SelectField(u'Beer of the Month Brewery Font:', coerce=int, option_widget=None)
    beerBomBreweryFontColor = StringField('Beer of the Month Brewery Color:')
    beerBomBreweryFontSize = SelectField(u'Beer of the Month Brewery Font Size:', coerce=int, option_widget=None)
    beerBomBreweryFontBoldToggle = BooleanField(u'Beer of the Month Brewery Bold:', default=False)
    beerBomBreweryFontItalicToggle = BooleanField(u'Beer of the Month Brewery Italic:', default=False)
    beerBomBreweryFontUnderlineToggle = BooleanField(u'Beer of the Month Brewery Underline:', default=False)

    beerBgColorOne = StringField('Background Color Code #1:')
    beerBgColorTwo = StringField('Background Color Code #2:')
    beerBgColorThree = StringField('Background Color Code #3:')
    beerBgColorFour = StringField('Background Color Code #4:')
    beerBgColorFive = StringField('Background Color Code #5:')
    beerBgColorDirection = SelectField(u'Background Font Color Direction:', option_widget=None)

    beerNameFont = SelectField(u'Beer Name Font:', coerce=int, option_widget=None)
    beerNameFontColor = StringField('Beer Name Font Color Code:')
    beerNameFontSize = SelectField(u'Beer Name Font Size:', coerce=int, option_widget=None)
    beerNameFontBoldToggle =  BooleanField(u'Beer Name Bold:', default=False)
    beerNameFontItalicToggle = BooleanField(u'Beer Name Italic:', default=False)
    beerNameFontUnderlineToggle = BooleanField(u'Beer Name Underline:', default=False)

    beerStyleFont = SelectField(u'Beer Style Font:', coerce=int, option_widget=None)
    beerStyleFontColor = StringField('Beer Style Font Color Code:')
    beerStyleFontSize = SelectField(u'Beer Style Font Size:', coerce=int, option_widget=None)
    beerStyleFontBoldToggle = BooleanField(u'Beer Style Bold:', default=False)
    beerStyleFontItalicToggle = BooleanField(u'Beer Style Italic:', default=False)
    beerStyleFontUnderlineToggle = BooleanField(u'Beer Style Underline:', default=False)

    beerAbvFontColor = StringField('Beer Abv Font Color Code:')
    beerAbvFontSize = SelectField(u'Beer Abv Font Size:', coerce=int, option_widget=None)
    beerAbvFontBoldToggle = BooleanField(u'Beer Abv Bold:', default=False)
    beerAbvFontItalicToggle = BooleanField(u'Beer Abv Italic:', default=False)
    beerAbvFontUnderlineToggle = BooleanField(u'Beer Abv Underline:', default=False)

    beerIbuFontColor = StringField('Beer Ibu Font Color Code:')
    beerIbuFontSize = SelectField(u'Beer Ibu Font Size:', coerce=int, option_widget=None)
    beerIbuFontBoldToggle = BooleanField(u'Beer Ibu Bold:', default=False)
    beerIbuFontItalicToggle = BooleanField(u'Beer Ibu Italic:', default=False)
    beerIbuFontUnderlineToggle = BooleanField(u'Beer Ibu Underline:', default=False)

    beerBreweryFont = SelectField(u'Beer Brewery Font:', coerce=int, option_widget=None)
    beerBreweryFontColor = StringField('Beer Brewery Font Color Code:')
    beerBreweryFontSize = SelectField(u'Beer Brewery Font Size:', coerce=int, option_widget=None)
    beerBreweryFontBoldToggle = BooleanField(u'Beer Brewery Bold:', default=False)
    beerBreweryFontItalicToggle = BooleanField(u'Beer Brewery Italic:', default=False)
    beerBreweryFontUnderlineToggle = BooleanField(u'Beer Brewery Underline:', default=False)

    beerTickerBgColorOne = StringField('Beer Ticker Background Color Code #1:')
    beerTickerBgColorTwo = StringField('Beer Ticker Background Color Code #2:')
    beerTickerBgColorThree = StringField('Beer Ticker Background Color Code #3:')
    beerTickerBgColorFour = StringField('Beer Ticker Background Color Code #4:')
    beerTickerBgColorFive = StringField('Beer Ticker Background Color Code #5:')
    beerTickerBgColorDirection = SelectField(u'Beer Ticker Background Font Color Direction:', option_widget=None)
    # font for beer names in the ticker
    beerTickerBeernamesFont = SelectField(u'Beer Ticker Names Font:', coerce=int, option_widget=None)

    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    beerTickerFont = SelectField(u'Beer Ticker Font:', coerce=int, option_widget=None)
    beerTickerFontColor = StringField('Beer Ticker Font Color:')
    beerTickerFontSize = SelectField(u'Beer Ticker Font Size:', coerce=int, option_widget=None)
    beerTickerFontBoldToggle = BooleanField(u'Beer Ticker Bold:', default=False)
    beerTickerFontItalicToggle = BooleanField(u'Beer Ticker Italic:', default=False)
    beerTickerFontUnderlineToggle = BooleanField(u'Beer Ticker Underline:', default=False)

    beerTickerToggle = BooleanField(u'Show Beer Ticker:', default=False)
    beerTickerScrollSpeed = IntegerField(u'Beer Ticker Scroll Speed:', [
        validators.DataRequired()
    ])

class WinecreenSettingsForm(FlaskForm):
    wineSettingsScreenId = SelectField(u'Screen Id', coerce=int, option_widget=None)
    winescreenTemplate = SelectField(u'Screen Template', [validators.optional()], coerce=int, option_widget=None)

    wineNameFont = SelectField(u'', coerce=int, option_widget=None)
    wineNameFontColor = StringField('')
    wineNameFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineNameFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineNameFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineNameFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineLocationFont = SelectField(u'', coerce=int, option_widget=None)
    wineLocationFontColor = StringField('')
    wineLocationFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineLocationFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineLocationFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineLocationFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineDescriptionFont = SelectField(u'', coerce=int, option_widget=None)
    wineDescriptionFontColor = StringField('')
    wineDescriptionFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineDescriptionFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineDescriptionFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineDescriptionFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineGlassFont = SelectField(u'', coerce=int, option_widget=None)
    wineGlassFontColor = StringField('')
    wineGlassFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineGlassFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineGlassFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineGlassFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineBottleFont = SelectField(u'', coerce=int, option_widget=None)
    wineBottleFontColor = StringField('')
    wineBottleFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineBottleFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineBottleFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineBottleFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineVarietalFont = SelectField(u'', coerce=int, option_widget=None)
    wineVarietalFontColor = StringField('')
    wineVarietalFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineVarietalFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineVarietalFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineVarietalFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineTypeFont = SelectField(u'', coerce=int, option_widget=None)
    wineTypeFontColor = StringField('')
    wineTypeFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineTypeFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineTypeFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineTypeFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineFoodPairingsFont = SelectField(u'', coerce=int, option_widget=None)
    wineFoodPairingsFontColor = StringField('')
    wineFoodPairingsFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineFoodPairingsFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineFoodPairingsFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineFoodpairingsFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineWebsiteFont = SelectField(u'', coerce=int, option_widget=None)
    wineWebsiteFontColor = StringField('')
    wineWebsiteFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineWebsiteFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineWebsiteFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineWebsiteFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineTickerBgColorOne = StringField('Background Color Code #1:')
    wineTickerBgColorTwo = StringField('Background Color Code #2:')
    wineTickerBgColorThree = StringField('Background Color Code #3:')
    wineTickerBgColorFour = StringField('Background Color Code #4:')
    wineTickerBgColorFive = StringField('Background Color Code #5:')
    wineTickerBgColorDirection = SelectField(u'Background Font Color Direction', coerce=int, option_widget=None)

    # font for wine names in the ticker
    wineTickerBeernamesFont = SelectField(u'', coerce=int, option_widget=None)
    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    wineTickerFont = SelectField(u'', coerce=int, option_widget=None)
    wineTickerFontColor = StringField('')
    wineTickerFontSize = SelectField(u'', coerce=int, option_widget=None)
    wineTickerFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    wineTickerFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    wineTickerFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    wineTickerToggle = BooleanField(u'Show Ticker:', default=False)
    wineTickerScrollSpeed =  IntegerField(u'Ticker Scroll Speed', [
        validators.DataRequired()
    ])

class EventscreenSettingsForm(FlaskForm):
    eventSettingsScreenId = SelectField(u'Screen Id', coerce=int, option_widget=None)
    eventscreenTemplate = SelectField(u'Screen Template', [validators.optional()], coerce=int, option_widget=None)


    eventNameFont = SelectField(u'', coerce=int, option_widget=None)
    eventNameFontColor = StringField('')
    eventNameFontSize = SelectField(u'', coerce=int, option_widget=None)
    eventNameFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    eventNameFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    eventNameFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    eventArtistFont = SelectField(u'', coerce=int, option_widget=None)
    eventArtistFontColor = StringField('')
    eventArtistFontSize = SelectField(u'', coerce=int, option_widget=None)
    eventArtistFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    eventArtistFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    eventArtistFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    eventDateofeventFont = SelectField(u'', coerce=int, option_widget=None)
    eventDateofeventFontColor = StringField('')
    eventDateofeventFontSize = SelectField(u'', coerce=int, option_widget=None)
    eventDateofeventFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    eventDateofeventFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    eventDateofeventFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    eventStarttimeFont = SelectField(u'', coerce=int, option_widget=None)
    eventStarttimeFontColor = StringField('')
    eventStarttimeFontSize = SelectField(u'', coerce=int, option_widget=None)
    eventStarttimeFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    eventStarttimeFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    eventStarttimeFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    eventEndtimeFont = SelectField(u'', coerce=int, option_widget=None)
    eventEndtimeFontColor = StringField('')
    eventEndtimeFontSize = SelectField(u'', coerce=int, option_widget=None)
    eventEndtimeFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    eventEndtimeFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    eventEndtimeFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    eventLocationFont = SelectField(u'', coerce=int, option_widget=None)
    eventLocationFontColor = StringField('')
    eventLocationFontSize = SelectField(u'', coerce=int, option_widget=None)
    eventLocationFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    eventLocationFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    eventLocationFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    eventTickerBgColorOne = StringField('Background Color Code One:')
    eventTickerBgColorTwo = StringField('Background Color Code Two:')
    eventTickerBgColorThree = StringField('Background Color Code Three:')
    eventTickerBgColorFour = StringField('Background Color Code Four:')
    eventTickerBgColorFive = StringField('Background Color Code Five:')
    eventTickerBgColorDirection = SelectField(u'Background Font Color Direction', coerce=int, option_widget=None)
    # font for event names in the ticker
    eventTickerBeernamesFont = SelectField(u'', coerce=int, option_widget=None)

    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    eventTickerFont = SelectField(u'', coerce=int, option_widget=None)
    eventTickerFontColor = StringField('')
    eventTickerFontSize = SelectField(u'', coerce=int, option_widget=None)
    eventTickerFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    eventTickerFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    eventTickerFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    eventTickerToggle = BooleanField(u'Show Ticker:', default=False)
    eventTickerScrollSpeed =  IntegerField(u'Ticker Scroll Speed', [
        validators.DataRequired()
    ])

class ItemscreenSettingsForm(FlaskForm):
    itemSettingsScreenId = SelectField(u'Screen Id', coerce=int, option_widget=None)
    itemscreenTemplate = SelectField(u'Screen Template', [validators.optional()], coerce=int, option_widget=None)

    itemNameFont = SelectField(u'', coerce=int, option_widget=None)
    itemNameFontColor = StringField('')
    itemNameFontSize = SelectField(u'', coerce=int, option_widget=None)
    itemNameFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    itemNameFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    itemNameFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    itemDescriptionFont = SelectField(u'', coerce=int, option_widget=None)
    itemDescriptionFontColor = StringField('')
    itemDescriptionFontSize = SelectField(u'', coerce=int, option_widget=None)
    itemDescriptionFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    itemDescriptionFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    itemDescriptionFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    itemPriceFont = SelectField(u'', coerce=int, option_widget=None)
    itemPriceFontColor = StringField('')
    itemPriceFontSize = SelectField(u'', coerce=int, option_widget=None)
    itemPriceFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    itemPriceFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    itemPriceFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    itemTickerBgColorOne = StringField('Background Color Code One:')
    itemTickerBgColorTwo = StringField('Background Color Code Two:')
    itemTickerBgColorThree = StringField('Background Color Code Three:')
    itemTickerBgColorFour = StringField('Background Color Code Four:')
    itemTickerBgColorFive = StringField('Background Color Code Five:')
    itemTickerBgColorDirection = SelectField(u'Background Font Color Direction', coerce=int, option_widget=None)

    # font for item names in the ticker
    itemTickerBeernamesFont = SelectField(u'', coerce=int, option_widget=None)

    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    itemTickerFont = SelectField(u'', coerce=int, option_widget=None)
    itemTickerFontColor = StringField('')
    itemTickerFontSize = SelectField(u'', coerce=int, option_widget=None)
    itemTickerFontBoldToggle = BooleanField(u'Show Ticker:', default=False)
    itemTickerFontItalicToggle = BooleanField(u'Show Ticker:', default=False)
    itemTickerFontUnderlineToggle = BooleanField(u'Show Ticker:', default=False)

    itemTickerToggle = BooleanField(u'Show Ticker:', default=False)
    itemTickerScrollSpeed =  IntegerField(u'Ticker Scroll Speed', [
        validators.DataRequired()
    ])

    itemTickerToggle = BooleanField(u'Show Ticker:', default=False)
    itemTickerScrollSpeed = IntegerField(u'Ticker Scroll Speed', [
        validators.DataRequired()
    ])


class FontSizeForm(FlaskForm):
    fontSizeOptions = DecimalField('Font Size Options (Min: 0.0 - Max: 5.0)', [validators.DataRequired(), validators.NumberRange(min=0, max=5.0)])
    fontSizes = SelectField(u'Font Sizes', [validators.optional()], coerce=int, option_widget=None)
class TemplateForm(FlaskForm):
    templateName = StringField('Name of Screen Template', [validators.Length(min=1, max=50)])
    templateSelect = SelectField(u'Templates', [validators.optional()], coerce=int, option_widget=None)

class DrinkContainerSizeForm(FlaskForm):
    drinkSizeText = StringField('Drink Size - 16oz Pint', [validators.Length(min=1, max=10)])
    drinkSizeSelect = SelectField(u'Drink Sizes', [validators.optional()], coerce=int, option_widget=None)

class DrinkPriceForm(FlaskForm):
    drinkPriceText = StringField('Drink Price - 5.00', [validators.Length(min=1, max=10)])
    drinkPriceSelect = SelectField(u'Drink Prices', [validators.optional()], coerce=int, option_widget=None)
