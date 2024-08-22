from flask import g, jsonify

from app import cache
from app.routes.api import api

@api.route("/hello")
@cache.cached(timeout=60, unless=lambda: not g.get('is_authorized', False))
def customers():

  if not g.get('is_authorized', False):
    return jsonify({'error': 'Unauthorized'}), 401
  
  return 'Hello, World!'