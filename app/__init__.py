from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
import logging
import config

cache = Cache(config={'CACHE_TYPE': config.CACHE_TYPE})

app = Flask(__name__)
CORS(app, origins="*")

cache.init_app(app)

from app import routes

# Setup console logging
if not app.debug:
  stream_handler = logging.StreamHandler()
  stream_handler.setLevel(logging.INFO)
  app.logger.addHandler(stream_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Flask App startup')
