#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/chaker/Dropbox/udacity/fsnd/catalog/")

from project import app as application
application.secret_key = 'Add your secret key'
