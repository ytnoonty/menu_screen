from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app
from menuscreen import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    venue_name = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    websiteURL = db.Column(db.String(200), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
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

    drink_size_options = db.relationship('Drink_sizes', backref='venue_id', lazy=True)
    drink_price_options = db.relationship('Drink_prices', backref='venue_id', lazy=True)

    beerscreen_settings = db.relationship('Beerscreen_settings', backref='venue_id', lazy=True)

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
    __tablename__ = 'list_history'
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
    # beer_logo_image_file = db.Column(db.LargeBinary, nullable=True)
    beer_logo_image_file_id = db.Column(db.Integer)
    # create_date = db.Column(db.DateTime, default=datetime.utcnow)
    size_id_1 = db.Column(db.Integer)
    price_id_1 = db.Column(db.Integer)
    size_id_2 = db.Column(db.Integer)
    price_id_2 = db.Column(db.Integer)
    size_id_3 = db.Column(db.Integer)
    price_id_3 = db.Column(db.Integer)
    size_id_4 = db.Column(db.Integer)
    price_id_4 = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ List_history: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} ***********'.format(self.id, self.name, self.style, self.abv, self.ibu, self.brewery, self.location, self.website, self.description, self.draft_bottle_selection, self.size_id_1, self.price_id_1, self.size_id_2, self.price_id_2, self.size_id_3, self.price_id_3, self.size_id_4, self.price_id_4, self.venue_db_id)
    # def __repr__(self):
    #     return '************ List_history: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} ***********'.format(self.id, self.name, self.style, self.abv, self.ibu, self.brewery, self.location, self.website, self.description, self.draft_bottle_selection, self.venue_db_id)

class Image_files(db.Model):
    __tablename__ = 'image_files'
    id = db.Column(db.Integer, primary_key=True)
    logo_image_file = db.Column(db.LargeBinary, nullable=True)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return '************ Image_files: {}, {}, {} ***********'.format(self.id, self.logo_image_file, self.venue_db_id)

class Drink_sizes(db.Model):
    __tablename__ = 'drink_sizes'
    id = db.Column(db.Integer, primary_key=True)
    drink_size = db.Column(db.String(100))
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return '************ Drink_sizes: {}, {}, {} ***********'.format(self.id, self.drink_size, self.venue_db_id)

class Drink_prices(db.Model):
    __tablename__ = 'drink_prices'
    id = db.Column(db.Integer, primary_key=True)
    drink_price = db.Column(db.String(100))
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return '************ Drink_prices: {}, {}, {} ***********'.format(self.id, self.drink_price, self.venue_db_id)

class List_current(db.Model):
    __tablename__ = 'list_current'
    id = db.Column(db.Integer, primary_key=True)
    id_history = db.Column(db.Integer)
    id_on_next = db.Column(db.Integer)
    id_dropdown = db.Column(db.Integer)
    beer_of_month = db.Column(db.Boolean, default=False)
    coming_soon = db.Column(db.Boolean, default=False)
    beer_screen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ List_current: {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id,self.id_history,self.id_on_next,self.id_dropdown,self.beer_of_month,self.coming_soon,self.beer_screen_id,self.venue_db_id)


class Beerscreen_settings(db.Model):
    __tablename__ = 'beerscreen_settings'
    id = db.Column(db.Integer, primary_key=True)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    beer_settings_screen_id = db.Column(db.Integer)
    beer_screen_template = db.Column(db.String(10))
    beer_screen_landscape_portrait_toggle = db.Column(db.Boolean, default=False)

    font_color_one = db.Column(db.String(10))
    font_color_two = db.Column(db.String(10))
    font_color_three = db.Column(db.String(10))
    font_color_direction = db.Column(db.String(100))
    shadow_font_color_one = db.Column(db.String(10))
    shadow_font_color_two = db.Column(db.String(10))
    shadow_font_color_three = db.Column(db.String(10))
    shadow_font_color_direction = db.Column(db.String(100))

    beer_bom_background_color_one = db.Column(db.String(10))
    beer_bom_background_color_two = db.Column(db.String(10))
    beer_bom_background_color_three = db.Column(db.String(10))
    beer_bom_background_color_four = db.Column(db.String(10))
    beer_bom_background_color_five = db.Column(db.String(10))
    beer_bom_background_color_direction = db.Column(db.String(100))

    beer_bom_name_font = db.Column(db.Integer)
    beer_bom_name_font_color = db.Column(db.String(10))
    beer_bom_name_font_size = db.Column(db.Integer)
    beer_bom_name_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_bom_name_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_bom_name_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_bom_style_font = db.Column(db.Integer)
    beer_bom_style_font_color = db.Column(db.String(10))
    beer_bom_style_font_size = db.Column(db.Integer)
    beer_bom_style_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_bom_style_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_bom_style_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_bom_abv_font_color = db.Column(db.String(10))
    beer_bom_abv_font_size = db.Column(db.Integer)
    beer_bom_abv_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_bom_abv_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_bom_abv_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_bom_ibu_font_color = db.Column(db.String(10))
    beer_bom_ibu_font_size = db.Column(db.Integer)
    beer_bom_ibu_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_bom_ibu_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_bom_ibu_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_bom_brewery_font = db.Column(db.Integer)
    beer_bom_brewery_font_color = db.Column(db.String(10))
    beer_bom_brewery_font_size = db.Column(db.Integer)
    beer_bom_brewery_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_bom_brewery_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_bom_brewery_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_background_color_one = db.Column(db.String(10))
    beer_background_color_two = db.Column(db.String(10))
    beer_background_color_three = db.Column(db.String(10))
    beer_background_color_four = db.Column(db.String(10))
    beer_background_color_five = db.Column(db.String(10))
    beer_background_color_direction = db.Column(db.String(100))

    beer_name_font = db.Column(db.Integer)
    beer_name_font_color = db.Column(db.String(10))
    beer_name_font_size = db.Column(db.Integer)
    beer_name_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_name_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_name_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_style_font = db.Column(db.Integer)
    beer_style_font_color = db.Column(db.String(10))
    beer_style_font_size = db.Column(db.Integer)
    beer_style_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_style_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_style_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_abv_font_color = db.Column(db.String(10))
    beer_abv_font_size = db.Column(db.Integer)
    beer_abv_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_abv_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_abv_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_ibu_font_color = db.Column(db.String(10))
    beer_ibu_font_size = db.Column(db.Integer)
    beer_ibu_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_ibu_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_ibu_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_brewery_font = db.Column(db.Integer)
    beer_brewery_font_color = db.Column(db.String(10))
    beer_brewery_font_size = db.Column(db.Integer)
    beer_brewery_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_brewery_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_brewery_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_ticker_bg_color_one = db.Column(db.String(10))
    beer_ticker_bg_color_two = db.Column(db.String(10))
    beer_ticker_bg_color_three = db.Column(db.String(10))
    beer_ticker_bg_color_four = db.Column(db.String(10))
    beer_ticker_bg_color_five = db.Column(db.String(10))
    beer_ticker_bg_color_direction = db.Column(db.String(100))
    # font for beer names in the ticker
    beer_ticker_beernames_font = db.Column(db.Integer)
    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    beer_ticker_font = db.Column(db.Integer)
    beer_ticker_font_color = db.Column(db.String(10))
    beer_ticker_font_size = db.Column(db.Integer)
    beer_ticker_font_bold_toggle = db.Column(db.Boolean, default=False)
    beer_ticker_font_italic_toggle = db.Column(db.Boolean, default=False)
    beer_ticker_font_underline_toggle = db.Column(db.Boolean, default=False)

    beer_ticker_toggle = db.Column(db.Boolean, default=False)
    beer_ticker_scroll_speed = db.Column(db.Integer)

    def __repr__(self):
        return '************ beer_settings: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id, self.venue_db_id, self.beer_settings_screen_id, self.beer_screen_template, self.beer_screen_landscape_portrait_toggle, self.font_color_one, self.font_color_two, self.font_color_three, self.font_color_direction, self.shadow_font_color_one, self.shadow_font_color_two, self.shadow_font_color_three, self.shadow_font_color_direction,  self.beer_bom_background_color_one, self.beer_bom_background_color_two, self.beer_bom_background_color_three, self.beer_bom_background_color_four, self.beer_bom_background_color_five, self.beer_bom_background_color_direction,  self.beer_bom_name_font, self.beer_bom_name_font_color, self.beer_bom_name_font_size, self.beer_bom_name_font_bold_toggle, self.beer_bom_name_font_italic_toggle, self.beer_bom_name_font_underline_toggle,  self.beer_bom_style_font, self.beer_bom_style_font_color, self.beer_bom_style_font_size, self.beer_bom_style_font_bold_toggle, self.beer_bom_style_font_italic_toggle, self.beer_bom_style_font_underline_toggle,  self.beer_bom_abv_font_color, self.beer_bom_abv_font_size, self.beer_bom_abv_font_bold_toggle, self.beer_bom_abv_font_italic_toggle, self.beer_bom_abv_font_underline_toggle,  self.beer_bom_ibu_font_color, self.beer_bom_ibu_font_size, self.beer_bom_ibu_font_bold_toggle, self.beer_bom_ibu_font_italic_toggle, self.beer_bom_ibu_font_underline_toggle,  self.beer_bom_brewery_font, self.beer_bom_brewery_font_color, self.beer_bom_brewery_font_size, self.beer_bom_brewery_font_bold_toggle, self.beer_bom_brewery_font_italic_toggle, self.beer_bom_brewery_font_underline_toggle,  self.beer_background_color_one, self.beer_background_color_two, self.beer_background_color_three, self.beer_background_color_four, self.beer_background_color_five, self.beer_background_color_direction,  self.beer_name_font, self.beer_name_font_color, self.beer_name_font_size, self.beer_name_font_bold_toggle, self.beer_name_font_italic_toggle, self.beer_name_font_underline_toggle,  self.beer_style_font, self.beer_style_font_color, self.beer_style_font_size, self.beer_style_font_bold_toggle, self.beer_style_font_italic_toggle, self.beer_style_font_underline_toggle,  self.beer_abv_font_color, self.beer_abv_font_size, self.beer_abv_font_bold_toggle, self.beer_abv_font_italic_toggle, self.beer_abv_font_underline_toggle,  self.beer_ibu_font_color, self.beer_ibu_font_size, self.beer_ibu_font_bold_toggle, self.beer_ibu_font_italic_toggle, self.beer_ibu_font_underline_toggle,  self.beer_brewery_font, self.beer_brewery_font_color, self.beer_brewery_font_size, self.beer_brewery_font_bold_toggle, self.beer_brewery_font_italic_toggle, self.beer_brewery_font_underline_toggle,  self.beer_ticker_bg_color_one, self.beer_ticker_bg_color_two, self.beer_ticker_bg_color_three, self.beer_ticker_bg_color_four, self.beer_ticker_bg_color_five, self.beer_ticker_bg_color_direction, # font for beer names in the ticker
        self.beer_ticker_beernames_font, self.beer_ticker_font, self.beer_ticker_font_color, self.beer_ticker_font_size, self.beer_ticker_font_bold_toggle, self.beer_ticker_font_italic_toggle, self.beer_ticker_font_underline_toggle,  self.beer_ticker_toggle, self.beer_ticker_scroll_speed)

class Winescreen_settings(db.Model):
    __tablename__ = 'winescreen_settings'
    id = db.Column(db.Integer, primary_key=True)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    wine_settings_screen_id = db.Column(db.Integer)
    wine_screen_template = db.Column(db.String(10))
    wine_screen_landscape_portrait_toggle = db.Column(db.Boolean, default=False)


    wine_name_font = db.Column(db.Integer)
    wine_name_font_color = db.Column(db.String(10))
    wine_name_font_size = db.Column(db.Integer)
    wine_name_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_name_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_name_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_location_font = db.Column(db.Integer)
    wine_location_font_color = db.Column(db.String(10))
    wine_location_font_size = db.Column(db.Integer)
    wine_location_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_location_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_location_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_description_font = db.Column(db.Integer)
    wine_description_font_color = db.Column(db.String(10))
    wine_description_font_size = db.Column(db.Integer)
    wine_description_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_description_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_description_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_glass_font = db.Column(db.Integer)
    wine_glass_font_color = db.Column(db.String(10))
    wine_glass_font_size = db.Column(db.Integer)
    wine_glass_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_glass_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_glass_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_bottle_font = db.Column(db.Integer)
    wine_bottle_font_color = db.Column(db.String(10))
    wine_bottle_font_size = db.Column(db.Integer)
    wine_bottle_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_bottle_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_bottle_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_varietal_font = db.Column(db.Integer)
    wine_varietal_font_color = db.Column(db.String(10))
    wine_varietal_font_size = db.Column(db.Integer)
    wine_varietal_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_varietal_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_varietal_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_type_font = db.Column(db.Integer)
    wine_type_font_color = db.Column(db.String(10))
    wine_type_font_size = db.Column(db.Integer)
    wine_type_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_type_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_type_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_foodPairings_font = db.Column(db.Integer)
    wine_foodPairings_font_color = db.Column(db.String(10))
    wine_foodPairings_font_size = db.Column(db.Integer)
    wine_foodPairings_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_foodPairings_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_foodPairings_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_website_font = db.Column(db.Integer)
    wine_website_font_color = db.Column(db.String(10))
    wine_website_font_size = db.Column(db.Integer)
    wine_website_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_website_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_website_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_ticker_bg_color_one = db.Column(db.String(10))
    wine_ticker_bg_color_two = db.Column(db.String(10))
    wine_ticker_bg_color_three = db.Column(db.String(10))
    wine_ticker_bg_color_four = db.Column(db.String(10))
    wine_ticker_bg_color_five = db.Column(db.String(10))
    wine_ticker_bg_color_direction = db.Column(db.String(100))
    # font for wine names in the ticker
    wine_ticker_beernames_font = db.Column(db.Integer)
    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    wine_ticker_font = db.Column(db.Integer)
    wine_ticker_font_color = db.Column(db.String(10))
    wine_ticker_font_size = db.Column(db.Integer)
    wine_ticker_font_bold_toggle = db.Column(db.Boolean, default=False)
    wine_ticker_font_italic_toggle = db.Column(db.Boolean, default=False)
    wine_ticker_font_underline_toggle = db.Column(db.Boolean, default=False)

    wine_ticker_toggle = db.Column(db.Boolean, default=False)
    wine_ticker_scroll_speed = db.Column(db.Integer)

    def __repr__(self):
        return '*****Wine_settings: {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(
        self.id,self.venue_db_id,self.wine_settings_screen_id,self.wines_creen_template,self.wines_screen_landscape_portrait_toggle,self.wine_name_font,self.wine_name_font_color,self.wine_name_font_size,self.wine_name_font_bold_toggle,self.wine_name_font_italic_toggle,self.wine_name_font_underline_toggle,self.wine_location_font,self.wine_location_font_color,self.wine_location_font_size,self.wine_location_font_bold_toggle,self.wine_location_font_italic_toggle,self.wine_location_font_underline_toggle,self.wine_description_font,self.wine_description_font_color,self.wine_description_font_size,self.wine_description_font_bold_toggle,self.wine_description_font_italic_toggle,self.wine_description_font_underline_toggle,self.wine_glass_font,self.wine_glass_font_color,self.wine_glass_font_size,self.wine_glass_font_bold_toggle,self.wine_glass_font_italic_toggle,self.wine_glass_font_underline_toggle,self.wine_bottle_font,self.wine_bottle_font_color,self.wine_bottle_font_size,self.wine_bottle_font_bold_toggle,self.wine_bottle_font_italic_toggle,self.wine_bottle_font_underline_toggle,self.wine_varietal_font,self.wine_varietal_font_color,self.wine_varietal_font_size,self.wine_varietal_font_bold_toggle,self.wine_varietal_font_italic_toggle,self.wine_varietal_font_underline_toggle,self.wine_type_font,self.wine_type_font_color,self.wine_type_font_size,self.wine_type_font_bold_toggle,self.wine_type_font_italic_toggle,self.wine_type_font_underline_toggle,self.wine_foodPairings_font,self.wine_foodPairings_font_color,self.wine_foodPairings_font_size,self.wine_foodPairings_font_bold_toggle,self.wine_foodPairings_font_italic_toggle,self.wine_foodPairings_font_underline_toggle,self.wine_website_font,self.wine_website_font_color,self.wine_website_font_size,self.wine_website_font_bold_toggle,self.wine_website_font_italic_toggle,self.wine_website_font_underline_toggle,self.wine_ticker_bg_color_one,self.wine_ticker_bg_color_two,self.wine_ticker_bg_color_three,self.wine_ticker_bg_color_four,self.wine_ticker_bg_color_five,self.wine_ticker_bg_color_direction,self.wine_ticker_beernames_font,self.wine_ticker_font,self.wine_ticker_font_color,self.wine_ticker_font_size,self.wine_ticker_font_bold_toggle,self.wine_ticker_font_italic_toggle,self.wine_ticker_font_underline_toggle, self.wine_ticker_toggle,self.wine_ticker_scroll_speed)

class Eventscreen_settings(db.Model):
    __tablename__ = 'eventscreen_settings'
    id = db.Column(db.Integer, primary_key=True)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_settings_screen_id = db.Column(db.Integer)
    event_screen_template = db.Column(db.String(10))
    event_screen_landscape_portrait_toggle = db.Column(db.Boolean, default=False)

    event_name_font = db.Column(db.Integer)
    event_name_font_color = db.Column(db.String(10))
    event_name_font_size = db.Column(db.Integer)
    event_name_font_bold_toggle = db.Column(db.Boolean, default=False)
    event_name_font_italic_toggle = db.Column(db.Boolean, default=False)
    event_name_font_underline_toggle = db.Column(db.Boolean, default=False)

    event_artist_font = db.Column(db.Integer)
    event_artist_font_color = db.Column(db.String(10))
    event_artist_font_size = db.Column(db.Integer)
    event_artist_font_bold_toggle = db.Column(db.Boolean, default=False)
    event_artist_font_italic_toggle = db.Column(db.Boolean, default=False)
    event_artist_font_underline_toggle = db.Column(db.Boolean, default=False)

    event_date_of_event_font = db.Column(db.Integer)
    event_date_of_event_font_color = db.Column(db.String(10))
    event_date_of_event_font_size = db.Column(db.Integer)
    event_date_of_event_font_bold_toggle = db.Column(db.Boolean, default=False)
    event_date_of_event_font_italic_toggle = db.Column(db.Boolean, default=False)
    event_date_of_event_font_underline_toggle = db.Column(db.Boolean, default=False)

    event_starttime_font = db.Column(db.Integer)
    event_starttime_font_color = db.Column(db.String(10))
    event_starttime_font_size = db.Column(db.Integer)
    event_starttime_font_bold_toggle = db.Column(db.Boolean, default=False)
    event_starttime_font_italic_toggle = db.Column(db.Boolean, default=False)
    event_starttime_font_underline_toggle = db.Column(db.Boolean, default=False)

    event_endtime_font = db.Column(db.Integer)
    event_endtime_font_color = db.Column(db.String(10))
    event_endtime_font_size = db.Column(db.Integer)
    event_endtime_font_bold_toggle = db.Column(db.Boolean, default=False)
    event_endtime_font_italic_toggle = db.Column(db.Boolean, default=False)
    event_endtime_font_underline_toggle = db.Column(db.Boolean, default=False)

    event_location_font = db.Column(db.Integer)
    event_location_font_color = db.Column(db.String(10))
    event_location_font_size = db.Column(db.Integer)
    event_location_font_bold_toggle = db.Column(db.Boolean, default=False)
    event_location_font_italic_toggle = db.Column(db.Boolean, default=False)
    event_location_font_underline_toggle = db.Column(db.Boolean, default=False)

    event_ticker_bg_color_one = db.Column(db.String(10))
    event_ticker_bg_color_two = db.Column(db.String(10))
    event_ticker_bg_color_three = db.Column(db.String(10))
    event_ticker_bg_color_four = db.Column(db.String(10))
    event_ticker_bg_color_five = db.Column(db.String(10))
    event_ticker_bg_color_direction = db.Column(db.String(100))
    # font for event names in the ticker
    event_ticker_beernames_font = db.Column(db.Integer)
    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    event_ticker_font = db.Column(db.Integer)
    event_ticker_font_color = db.Column(db.String(10))
    event_ticker_font_size = db.Column(db.Integer)
    event_ticker_font_bold_toggle = db.Column(db.Boolean, default=False)
    event_ticker_font_italic_toggle = db.Column(db.Boolean, default=False)
    event_ticker_font_underline_toggle = db.Column(db.Boolean, default=False)

    event_ticker_toggle = db.Column(db.Boolean, default=False)
    event_ticker_scroll_speed = db.Column(db.Integer)

class Itemscreen_settings(db.Model):
    __tablename__ = 'itemscreen_settings'
    id = db.Column(db.Integer, primary_key=True)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_settings_screen_id = db.Column(db.Integer)
    item_screen_template = db.Column(db.String(10))
    item_screen_landscape_portrait_toggle = db.Column(db.Boolean, default=False)

    item_name_font = db.Column(db.Integer)
    item_name_font_color = db.Column(db.String(10))
    item_name_font_size = db.Column(db.Integer)
    item_name_font_bold_toggle = db.Column(db.Boolean, default=False)
    item_name_font_italic_toggle = db.Column(db.Boolean, default=False)
    item_name_font_underline_toggle = db.Column(db.Boolean, default=False)

    item_description_font = db.Column(db.Integer)
    item_description_font_color = db.Column(db.String(10))
    item_description_font_size = db.Column(db.Integer)
    item_description_font_bold_toggle = db.Column(db.Boolean, default=False)
    item_description_font_italic_toggle = db.Column(db.Boolean, default=False)
    item_description_font_underline_toggle = db.Column(db.Boolean, default=False)

    item_price_font = db.Column(db.Integer)
    item_price_font_color = db.Column(db.String(10))
    item_price_font_size = db.Column(db.Integer)
    item_price_font_bold_toggle = db.Column(db.Boolean, default=False)
    item_price_font_italic_toggle = db.Column(db.Boolean, default=False)
    item_price_font_underline_toggle = db.Column(db.Boolean, default=False)

    item_ticker_bg_color_one = db.Column(db.String(10))
    item_ticker_bg_color_two = db.Column(db.String(10))
    item_ticker_bg_color_three = db.Column(db.String(10))
    item_ticker_bg_color_four = db.Column(db.String(10))
    item_ticker_bg_color_five = db.Column(db.String(10))
    item_ticker_bg_color_direction = db.Column(db.String(100))
    # font for item names in the ticker
    item_ticker_beernames_font = db.Column(db.Integer)
    # font for headings of ticker ie. 'Beer 'O the Month, Tapping Soon and Shamrock News:'
    item_ticker_font = db.Column(db.Integer)
    item_ticker_font_color = db.Column(db.String(10))
    item_ticker_font_size = db.Column(db.Integer)
    item_ticker_font_bold_toggle = db.Column(db.Boolean, default=False)
    item_ticker_font_italic_toggle = db.Column(db.Boolean, default=False)
    item_ticker_font_underline_toggle = db.Column(db.Boolean, default=False)

    item_ticker_toggle = db.Column(db.Boolean, default=False)
    item_ticker_scroll_speed = db.Column(db.Integer)

    def __repr__(self):
        return '************ Item_settings: {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(self.id, self.venue_db_id, self.item_settings_screen_id, self.item_screen_template, self.item_screen_landscape_portrait_toggle,
        self.item_name_font, self.item_name_font_color, self.item_name_font_size, self.item_name_font_bold_toggle, self.item_name_font_italic_toggle, self.item_name_font_underline_toggle, self.item_description_font, self.item_description_font_color, self.item_description_font_size, self.item_description_font_bold_toggle, self.item_description_font_italic_toggle, self.item_description_font_underline_toggle, self.item_price_font, self.item_price_font_color, self.item_price_font_size, self.item_price_font_bold_toggle, self.item_price_font_italic_toggle, self.item_price_font_underline_toggle, self.item_ticker_bg_color_one, self.item_ticker_bg_color_two, self.item_ticker_bg_color_three, self.item_ticker_bg_color_four, self.item_ticker_bg_color_five, self.item_ticker_bg_color_direction, self.item_ticker_beernames_font, self.item_ticker_font, self.item_ticker_font_color, self.item_ticker_font_size, self.item_ticker_font_bold_toggle, self.item_ticker_font_italic_toggle, self.item_ticker_font_underline_toggle, self.item_ticker_toggle, self.item_ticker_scroll_speed, self.settings_screen_id, self.screen_template, self.venue_db_id)



class Ticker(db.Model):
    __tablename__= 'ticker'
    id = db.Column(db.Integer, primary_key=True)
    ticker_text = db.Column(db.Text)
    ticker_screen_id = db.Column(db.Integer)
    ticker_type = db.Column(db.Integer)
    ticker_type_id = db.relationship('Ticker_type_id', backref='ticker_type_id', lazy=True)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Ticker: {}, {}, {}'.format(self.id,self.ticker_text,self.tickerscreen_id,self.venue_db_id)

class Ticker_type_id(db.Model):
    __tablename__= 'ticker_type_id'
    id = db.Column(db.Integer, primary_key=True)
    ticker_type = db.Column(db.String(25))
    ticker_type_id_fk = db.Column(db.Integer, db.ForeignKey('ticker.id'), nullable=False)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ TickerTypeId: {}, {}, {}'.format(self.id, self.ticker_type, self.venue_db_id)

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
    template_screen_id = db.Column(db.Integer)
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
    food_pairings = db.Column(db.Text)
    website = db.Column(db.String(100))
    wine_screen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Wines: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id,self.venue_db_id,self.name,self.location,self.description,self.glass,self.bottle,self.varietal,self.type,self.food_pairings)

class Winelist_current(db.Model):
    __tablename__ = 'winelist_current'
    id = db.Column(db.Integer, primary_key=True)
    id_wine = db.Column(db.Integer)
    id_dropdown = db.Column(db.Integer)
    wine_screen_id = db.Column(db.Integer)
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
    event_screen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Event: {}, {}, {}, {}, {}'.format(self.id, self.name, self.artist, self.date_of_event, self.starttime_of_event, self.endtime_of_event, self.location, self.venue_db_id)

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.String(100))
    item_screen_id = db.Column(db.Integer)
    venue_db_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '************ Item: {}, {}, {}, {}, {} ***********'.format(self.id, self.name, self.description, self.price, self.venue_db_id)
