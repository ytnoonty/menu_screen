from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, IntegerField, BooleanField, validators
from wtforms.validators import DataRequired

class BeerscreenSettingsForm(FlaskForm):
    beerSettingsScreenId = SelectField(u'Screen Id', coerce=int, option_widget=None)
    beerscreenTemplate = SelectField(u'Screen Template', [validators.optional()], coerce=int, option_widget=None)

    fontColorOne = StringField('Font Color Code One:')
    fontColorTwo = StringField('Font Color Code Two')
    fontColorThree = StringField('Font Color Code Three')
    fontColorDirection = SelectField('Font Color Direction')
    shadowFontColorOne = StringField('Shadow Font Color Code One:')
    shadowFontColorTwo = StringField('Shadow Font Color Code Two')
    shadowFontColorThree = StringField('Shadow Font Color Code Three')
    shadowFontColorDirection = SelectField('Shadow Font Color Direction')

    beerBomBgColorOne = StringField('Beer of the Month Background Color Code One:')
    beerBomBgColorTwo = StringField('Beer of the Month Background Color Code Two:')
    beerBomBgColorThree = StringField('Beer of the Month Background Color Code Three:')
    beerBomBgColorFour = StringField('Beer of the Month Background Color Code Four:')
    beerBomBgColorFive = StringField('Beer of the Month Background Color Code Five:')
    beerBomBgColorDirection = SelectField(u'Beer of the Month Background Color Direction', option_widget=None)

    beerBomNameFont = SelectField(u'Beer of the Month Name Font', coerce=int, option_widget=None)
    beerBomNameFontColor = StringField('Beer of the Month Name Font Color')
    beerBomNameFontSize = SelectField(u'Beer of the Month Name Font Size', coerce=int, option_widget=None)
    beerBomNameFontBoldToggle = BooleanField(u'Name Bold Font:', default=False)
    beerBomNameFontItalicToggle = BooleanField(u'Name Italic:', default=False)
    beerBomNameFontUnderlineToggle = BooleanField(u'Name Underline:', default=False)

    beerBomStyleFont = SelectField(u'Beer of the Month Style Font', coerce=int, option_widget=None)
    beerBomStyleFontColor = StringField('Beer of the Month Style Color')
    beerBomStyleFontSize = SelectField(u'Beer of the Month Style Font Size', coerce=int, option_widget=None)
    beerBomStyleFontBoldToggle = BooleanField(u'Beer of the Month Style Bold Font:', default=False)
    beerBomStyleFontItalicToggle = BooleanField(u'Beer of the Month Style Italic:', default=False)
    beerBomStyleFontUnderlineToggle = BooleanField(u'Beer of the Month Style Underline:', default=False)

    beerBomAbvFontColor = StringField('Beer of the Month ABV Font Color')
    beerBomAbvFontSize = SelectField(u'Beer of the Month ABV Font size', coerce=int, option_widget=None)
    beerBomAbvFontBoldToggle = BooleanField(u'Beer of the Month ABV Bold Font:', default=False)
    beerBomAbvFontItalicToggle = BooleanField(u'Beer of the Month ABV Italic:', default=False)
    beerBomAbvFontUnderlineToggle = BooleanField(u'Beer of the Month ABV Underline:', default=False)

    beerBomIbuFontColor = StringField('Beer of the Month IBU Font Color')
    beerBomIbuFontSize = SelectField(u'Beer of the Month IBU Font Size', coerce=int, option_widget=None)
    beerBomIbuFontBoldToggle = BooleanField(u'Beer of the Month IBU Bold Font:', default=False)
    beerBomIbuFontItalicToggle = BooleanField(u'Beer of the Month IBU Italic:', default=False)
    beerBomIbuFontUnderlineToggle = BooleanField(u'Beer of the Month IBU Underline:', default=False)

    beerBomBreweryFont = SelectField(u'Beer of the Month Brewery Font', coerce=int, option_widget=None)
    beerBomBreweryFontColor = StringField('Beer of the Month Brewery Color')
    beerBomBreweryFontSize = SelectField(u'Beer of the Month Brewery Font size', coerce=int, option_widget=None)
    beerBomBreweryFontBoldToggle = BooleanField(u'Beer of the Month Brewery Bold Font:', default=False)
    beerBomBreweryFontItalicToggle = BooleanField(u'Beer of the Month Brewery Italic:', default=False)
    beerBomBreweryFontUnderlineToggle = BooleanField(u'Beer of the Month Brewery Underline:', default=False)

    beerBgColorOne = StringField('Background Color Code #1:')
    beerBgColorTwo = StringField('Background Color Code #2:')
    beerBgColorThree = StringField('Background Color Code #3:')
    beerBgColorFour = StringField('Background Color Code #4:')
    beerBgColorFive = StringField('Background Color Code #5:')
    beerBgColorDirection = SelectField(u'Background Font Color Direction', option_widget=None)

    beerNameFont = SelectField(u'Beer Name font', coerce=int, option_widget=None)
    beerNameFontColor = StringField('Beer Name font color')
    beerNameFontSize = SelectField(u'Beer Name font size', coerce=int, option_widget=None)
    beerNameFontBoldToggle =  BooleanField(u'Beer Name Bold Font:', default=False)
    beerNameFontItalicToggle = BooleanField(u'Beer Name Italic:', default=False)
    beerNameFontUnderlineToggle = BooleanField(u'Beer Name Underline:', default=False)

    beerStyleFont = SelectField(u'Beer Style font', coerce=int, option_widget=None)
    beerStyleFontColor = StringField('Beer Style font color')
    beerStyleFontSize = SelectField(u'Beer Style font size', coerce=int, option_widget=None)
    beerStyleFontBoldToggle = BooleanField(u'Beer Style Bold Font:', default=False)
    beerStyleFontItalicToggle = BooleanField(u'Beer Style Italic:', default=False)
    beerStyleFontUnderlineToggle = BooleanField(u'Beer Style Underline:', default=False)

    beerAbvFontColor = StringField('Beer ABV font color')
    beerAbvFontSize = SelectField(u'Beer ABV font size', coerce=int, option_widget=None)
    beerAbvFontBoldToggle = BooleanField(u'Beer ABV Bold Font:', default=False)
    beerAbvFontItalicToggle = BooleanField(u'Beer ABV Italic:', default=False)
    beerAbvFontUnderlineToggle = BooleanField(u'Beer ABV Underline:', default=False)

    beerIbuFontColor = StringField('Beer IBU font color')
    beerIbuFontSize = SelectField(u'Beer IBU font size', coerce=int, option_widget=None)
    beerIbuFontBoldToggle = BooleanField(u'Beer IBU Bold font:', default=False)
    beerIbuFontItalicToggle = BooleanField(u'Beer IBU Italic:', default=False)
    beerIbuFontUnderlineToggle = BooleanField(u'Beer IBU Underline:', default=False)

    beerBreweryFont = SelectField(u'Beer Brewery font', coerce=int, option_widget=None)
    beerBreweryFontColor = StringField('Beer Brewery font color')
    beerBreweryFontSize = SelectField(u'Beer Brewery font size', coerce=int, option_widget=None)
    beerBreweryFontBoldToggle = BooleanField(u'Beer Brewery Bold Font:', default=False)
    beerBreweryFontItalicToggle = BooleanField(u'Beer Brewery Italic:', default=False)
    beerBreweryFontUnderlineToggle = BooleanField(u'Beer Brewery Underline:', default=False)

    beerTickerBgColorOne = StringField('Ticker Background Color Code One:')
    beerTickerBgColorTwo = StringField('Ticker Background Color Code Two:')
    beerTickerBgColorThree = StringField('Ticker Background Color Code Three:')
    beerTickerBgColorFour = StringField('Ticker Background Color Code Four:')
    beerTickerBgColorFive = StringField('Ticker Background Color Code Five:')
    beerTickerBgColorDirection = SelectField(u'Ticker Background Font Color Direction', option_widget=None)
    # font for beer names in the ticker
    beerTickerBeernamesFont = SelectField(u'Beer Ticker Names Font', coerce=int, option_widget=None)

    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    beerTickerFont = SelectField(u'Beer Ticker Font', coerce=int, option_widget=None)
    beerTickerFontColor = StringField('Beer Ticker Font color')
    beerTickerFontSize = SelectField(u'Beer Ticker Font size', coerce=int, option_widget=None)
    beerTickerFontBoldToggle = BooleanField(u'Beer Ticker Bold Font:', default=False)
    beerTickerFontItalicToggle = BooleanField(u'Beer Ticker Italic:', default=False)
    beerTickerFontUnderlineToggle = BooleanField(u'Beer Ticker Underline:', default=False)

    beerTickerToggle = BooleanField(u'Show Beer Ticker:', default=False)
    beerTickerScrollSpeed = IntegerField(u'Beer Ticker Scroll Speed', [
        validators.DataRequired()
    ])

class WinescreenSettingsForm(FlaskForm):
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
