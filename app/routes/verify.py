import secrets

from flask import request, g
import config

from app import app

def verify_api_key(api_key):
  return secrets.compare_digest(api_key, config.API_KEY)

@app.before_request
def check_authorization():
  api_key = request.headers.get('Authorization')
    
  if api_key and api_key.startswith('Bearer '):
    token = api_key.split(' ')[1]
    if verify_api_key(token):
      g.is_authorized = True
      return
  g.is_authorized = False
