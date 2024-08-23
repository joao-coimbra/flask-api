from flask import g

from app import cache
from app.routes.api import api

@api.route("/hello")
@cache.cached(timeout=60, unless=lambda: not g.get('is_authorized', False))
def hello():
  
  return 'Hello, World!'