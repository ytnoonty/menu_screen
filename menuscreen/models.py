from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app
from menuscreen import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    beerlist_history = db.relationship('List_history', backref='venue_id', lazy=True)
    beerlist_sort_asc = db.relationship('List_history', order_by='List_history.name')

    beerlist_current = db.relationship('List_current', backref='venue_id', lazy=True)

    winelist_history = db.relationship('Wines', backref='venue_id', lazy=True)
    winelist_sort_asc = db.relationship('Wines', order_by='Wines.name')
    winelist_current = db.relationship('Winelist_current', backref='venue_id', lazy=True)
    winelist_current_sort_asc = db.relationship('Winelist_current', order_by='Winelist_current.id_dropdown')

    font_size_options = db.relationship('Font_size_options', backref='venue_id', lazy=True)
    templates = db.relationship('Template', backref='venue_id', lazy=True)

    user_settings = db.relationship('User_settings', backref='venue_id', lazy=True)

    event = db.relationship('Event', backref='venue_id', lazy=True)
    event_sort_asc = db.relationship('Event', order_by='Event.date_of_event')

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return '************ User: {}, {}, {}, {}, {}'.format(self.venue_name, self.name, self.email, self.username, self.image_file)

    # userss = Users(name='aman', venue_name='anam', email='test@email.com', username='testuser', password='pasword')

class List_history(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(100), nullable=False)
    abv = db.Column(db.String(10))
    ibu = db.Column(db.String(10))
    brewery = db.Column(db.String(100))
    location = db.Column(db.String(100))
    website = db.Column(db.String(255))
    description = db.Column(db.Text)
    draft_bottle_selection = db.Column(db.String(50))
    # create_date = db.Column(db.DateTime, default=datetime.utcnow)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ List_history: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} ***********'.format(self.id, self.name, self.style, self.abv, self.ibu, self.brewery, self.location, self.website, self.description, self.draft_bottle_selection, self.venue_db_id)
    # list = List_history(name='TestName', style='TestStyle', venue_db_id='1')


class List_current(db.Model):
    __tablename__ = 'list_current'
    id = db.Column(db.Integer, primary_key=True)
    id_history = db.Column(db.Integer)
    id_on_next = db.Column(db.Integer)
    id_dropdown = db.Column(db.Integer)
    beer_of_month = db.Column(db.Boolean, default=False)
    coming_soon = db.Column(db.Boolean, default=False)
    beerscreen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ List_current: {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id,self.id_history,self.id_on_next,self.id_dropdown,self.beer_of_month,self.coming_soon,self.beerscreen_id,self.venue_db_id)


class User_settings(db.Model):
    __tablename__ = 'user_settings'
    id = db.Column(db.Integer, primary_key=True)
    number_of_screens = db.Column(db.String(10), nullable=False)
    beerscreen_settings_id = db.Column(db.String(10), nullable=False)
    font_color_one = db.Column(db.String(100))
    font_color_two = db.Column(db.String(100))
    font_color_three = db.Column(db.String(100))
    font_color_direction = db.Column(db.String(100))
    shadow_font_color_one = db.Column(db.String(100))
    shadow_font_color_two = db.Column(db.String(100))
    shadow_font_color_three = db.Column(db.String(100))
    shadow_font_color_direction = db.Column(db.String(100))
    background_color_one = db.Column(db.String(100))
    background_color_two = db.Column(db.String(100))
    background_color_three = db.Column(db.String(100))
    background_color_direction = db.Column(db.String(100))
    name_font_color = db.Column(db.String(10))
    style_font_color = db.Column(db.String(10))
    abv_font_color = db.Column(db.String(10))
    ibu_font_color = db.Column(db.String(10))
    brewery_font_color = db.Column(db.String(10))
    name_font_size = db.Column(db.String(10))
    style_font_size = db.Column(db.String(10))
    abv_font_size = db.Column(db.String(10))
    ibu_font_size = db.Column(db.String(10))
    brewery_font_size = db.Column(db.String(10))
    screen_template = db.Column(db.String(10))
    ticker_toggle = db.Column(db.Boolean, default=False)
    ticker_scroll_speed = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ User_settings: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id, self.venue_db_id, self.font_color_one, self.font_color_two, self.font_color_three, self.font_color_direction, self.shadow_font_color_one, self.shadow_font_color_two, self.shadow_font_color_three, self.shadow_font_color_direction, self.background_color_one, self.background_color_two, self.background_color_three, self.background_color_direction, self.name_font_color, self.abv_font_color, self.ibu_font_color, self.brewery_font_color, self.name_font_size, self.abv_font_size, self.ibu_font_size, self.brewery_font_size, self.screen_template)

class Ticker(db.Model):
    __tablename__= 'ticker'
    id = db.Column(db.Integer, primary_key=True)
    ticker_text = db.Column(db.Text)
    tickerscreen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Ticker: {}, {}, {}'.format(self.id,self.ticker_text,self.tickerscreen_id,self.venue_db_id)

class Font_size_options(db.Model):
    __tablename__ = 'font_size_options'
    id = db.Column(db.Integer, primary_key=True)
    font_sizes = db.Column(db.String(100))
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Font_size_options: {}, {}, {}'.format(self.id,self.venue_db_id,self.font_sizes)

class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True)
    template_name = db.Column(db.String(255))
    screen_number = db.Column(db.Integer)
    active_template = db.Column(db.String(100))
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Templates: {}, {}, {}, {}, {}'.format(self.id,self.template_name,self.venue_db_id,self.screen_number,self.active_template)

class Wines(db.Model):
    __tablename__ = 'wines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.Text)
    glass = db.Column(db.String(10))
    bottle = db.Column(db.String(10))
    varietal = db.Column(db.String(100))
    type = db.Column(db.Integer)
    foodPairings = db.Column(db.Text)
    website = db.Column(db.String(100))
    winescreen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Wines: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id,self.venue_db_id,self.name,self.location,self.description,self.glass,self.bottle,self.varietal,self.type,self.foodPairings)

class Winelist_current(db.Model):
    __tablename__ = 'winelist_current'
    id = db.Column(db.Integer, primary_key=True)
    id_wine = db.Column(db.Integer)
    id_dropdown = db.Column(db.Integer)
    winescreen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Winelist_current: {}, {}, {}, {}'.format(self.id,self.venue_db_id,self.id_wine,self.id_dropdown)

class Wine_type(db.Model):
    __tablename__ = 'wine_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Wine_type: {}, {}'.format(self.id, self.type)

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100))
    date_of_event = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    starttime_of_event = db.Column(db.String(10), nullable=False)
    endtime_of_event = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(255))
    eventscreen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Event: {}, {}, {}, {}, {}'.format(self.id, self.name, self.artist, self.date_of_event, self.starttime_of_event, self.endtime_of_event, self.location, self.venue_db_id)

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.String(100))
    itemscreen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Item: {}, {}, {}, {}, {} ***********'.format(self.id, self.name, self.description, self.price, self.venue_db_id)
