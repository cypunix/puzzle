import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(1, '/usr/src/app')

from flaskapp import app as application
