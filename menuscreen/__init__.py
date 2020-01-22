import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from menuscreen.config import Config

# from passlib.hash import sha256_crypt
from functools import wraps
import datetime
import feedparser
import json



# #######################################
# #PUSHER
import pusher
pusher_client = pusher.Pusher(
    #development info
    app_id='774716',
    key='55b76ba88af32c57990c',
    secret='6615b9606b368a9aca74',
    cluster='us2',
    ssl=True
)
# #PUSHER
# #######################################


# ###################
# # serversent evnets
# from flask_sse import sse
# ###################

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)
    mail.init_app(app)

    from menuscreen.users.routes import users
    from menuscreen.displays.routes import displays
    from menuscreen.list_history.routes import list_history
    from menuscreen.main.routes import main
    from menuscreen.event.routes import event
    from menuscreen.wine.routes import wine
    from menuscreen.settttings.routes import settttings
    from menuscreen.image.routes import image
    from menuscreen.errors.handlers import errors
    # from menuscreen.streams.routes import streams

    app.register_blueprint(users)
    app.register_blueprint(displays)
    app.register_blueprint(list_history)
    app.register_blueprint(main)
    app.register_blueprint(event)
    app.register_blueprint(wine)
    app.register_blueprint(settttings)
    app.register_blueprint(image)
    app.register_blueprint(errors)
    # app.register_blueprint(streams)

    return app
