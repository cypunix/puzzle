import sys
import logging
logging.basicConfig(stream=sys.stderr)
#sys.path.insert(0, '/var/www/html/flaskapp')
sys.path.insert(1, '/home/cyp/git/webappp')

from flaskapp import app as application
