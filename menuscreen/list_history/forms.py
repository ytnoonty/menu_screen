from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired

# Beer Form Class
class BeerForm(FlaskForm):
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=3, max=100)
    ])
    style = StringField('Style', [
        validators.Length(min=0, max=50)
    ])
    abv = StringField('Abv', [
        validators.Length(min=0, max=10)
    ])
    ibu = StringField('Ibu', [
        validators.Length(min=0, max=10)
    ])
    brewery = StringField('Brewery', [
        validators.Length(min=0, max=100)
    ])
    location = StringField('Location', [
        validators.Length(min=0, max=255)
    ])
    website = StringField('Website', [
        validators.Length(min=0, max=255)
    ])
    description = TextAreaField('Description', [
        validators.Length(min=0)
    ])
#########################radio button to choose draft or bottle or both
    draftBottle = RadioField(u'Beer Choice', choices=[('Draft','Draft'), ('Bottle','Bottle'), ('Can','Can'), ('Draft & Bottle',' Draft & Bottle'), ('Draft & Can','Draft & Can'), ('Bottle & Can','Bottle & Can'), ('Draft, Bottle & Can','Draft, Bottle & Can')])

    # # WTF validation method to find if duplicate name
    # def validate_name(self, name):
    #     if name.data != current_user.name:
    #         user = User.query.filter_by(name=name.data).first()
    #         if user:
    #             raise ValidationError('This Beer is alread in the system. Please change the name or edit the information.')

# Class for the beer list
class CurrentBeerListForm(FlaskForm):
    beer_1 = SelectField(u'Beer 1', coerce=int, option_widget=None)
    beer_2 = SelectField(u'Beer 2', coerce=int, option_widget=None)
    beer_3 = SelectField(u'Beer 3', coerce=int, option_widget=None)
    beer_4 = SelectField(u'Beer 4', coerce=int, option_widget=None)
    beer_5 = SelectField(u'Beer 5', coerce=int, option_widget=None)
    beer_6 = SelectField(u'Beer 6', coerce=int, option_widget=None)
    beer_7 = SelectField(u'Beer 7', coerce=int, option_widget=None)
    beer_8 = SelectField(u'Beer 8', coerce=int, option_widget=None)
    beer_9 = SelectField(u'Beer 9', coerce=int, option_widget=None)
    beer_10 = SelectField(u'Beer 10', coerce=int, option_widget=None)
    beer_11 = SelectField(u'Beer 11', coerce=int, option_widget=None)
    beer_12 = SelectField(u'Beer 12', coerce=int, option_widget=None)
    beer_13 = SelectField(u'Beer 13', coerce=int, option_widget=None)
    beer_14 = SelectField(u'Beer 14', coerce=int, option_widget=None)
    beer_15 = SelectField(u'Beer 15', coerce=int, option_widget=None)
    beer_16 = SelectField(u'Beer 16', coerce=int, option_widget=None)
    beer_17 = SelectField(u'Beer 17', coerce=int, option_widget=None)
    beer_18 = SelectField(u'Beer 18', coerce=int, option_widget=None)
    beer_19 = SelectField(u'Beer 19', coerce=int, option_widget=None)
    beer_20 = SelectField(u'Beer 20', coerce=int, option_widget=None)
    beer_21 = SelectField(u'Beer 21', coerce=int, option_widget=None)
    #tickerHeadline
    beer_22 = SelectField(u'Ticker Headline', coerce=int, option_widget=None)

# Class for the beer_ list
class NextBeerListForm(FlaskForm):
    beer_1 = SelectField(u'Beer 1', coerce=int, option_widget=None)
    beer_2 = SelectField(u'Beer 2', coerce=int, option_widget=None)
    beer_3 = SelectField(u'Beer 3', coerce=int, option_widget=None)
    beer_4 = SelectField(u'Beer 4', coerce=int, option_widget=None)
    beer_5 = SelectField(u'Beer 5', coerce=int, option_widget=None)
    beer_6 = SelectField(u'Beer 6', coerce=int, option_widget=None)
    beer_7 = SelectField(u'Beer 7', coerce=int, option_widget=None)
    beer_8 = SelectField(u'Beer 8', coerce=int, option_widget=None)
    beer_9 = SelectField(u'Beer 9', coerce=int, option_widget=None)
    beer_10 = SelectField(u'Beer 10', coerce=int, option_widget=None)
    beer_11 = SelectField(u'Beer 11', coerce=int, option_widget=None)
    beer_12 = SelectField(u'Beer 12', coerce=int, option_widget=None)
    beer_13 = SelectField(u'Beer 13', coerce=int, option_widget=None)
    beer_14 = SelectField(u'Beer 14', coerce=int, option_widget=None)
    beer_15 = SelectField(u'Beer 15', coerce=int, option_widget=None)
    beer_16 = SelectField(u'Beer 16', coerce=int, option_widget=None)
