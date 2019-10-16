import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
    REDIS_URL = "redis://localhost"
