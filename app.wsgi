#!/usr/bin/python3.6
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/twapp/')

from app import app as application
application.secret_key = 'secret'