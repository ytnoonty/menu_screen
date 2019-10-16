import os

class Config:
    SECRET_KEY = '760569b703c89422c18038412d44704aad69f0d90eed673b36b049c1e2a4c130'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Chewboka_123@localhost/myflaskapp'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = 'testingAPPtechnology@gmail.com'
    MAIL_PASSWORD = 'testingAPPtech!@#$'
