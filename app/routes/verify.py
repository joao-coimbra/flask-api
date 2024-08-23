from datetime import datetime
import secrets

from flask import jsonify, request, g
import config

from app.routes.api import api

def verify_api_key(api_key):
  return secrets.compare_digest(api_key, config.API_KEY)

@api.before_request
def check_authorization():
  api_key = request.headers.get('Authorization')
    
  if api_key and api_key.startswith('Bearer '):
    token = api_key.split(' ')[1]
    if verify_api_key(token):
      g.is_authorized = True
      return
  g.is_authorized = False
  return jsonify({'error': 'Unauthorized'}), 401