#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/FlaskApp/menu_screen/')

from run import app as application
application.secret_key = '760569b703c89422c18038412d44704aad69f0d90pieed673b36b049c1e2a4c130'
