import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = os.getenv('FLASK_ENV', 'production')
API_KEY=os.getenv('API_KEY')

DEBUG = True  # some Flask specific configs
CACHE_TYPE = "SimpleCache"  # Flask-Caching related configs
CACHE_DEFAULT_TIMEOUT = 300