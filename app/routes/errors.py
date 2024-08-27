from flask import json
from app import app
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
  response = e.get_response()
    # replace the body with JSON
  response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
  response.content_type = "application/json"
  return response