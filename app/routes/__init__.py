from datetime import datetime
import os
from flask import render_template, send_from_directory
from app import app
from app.routes.api import api

from app.routes import verify

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
  current_year = datetime.now().year

  return render_template('hello.html', current_year=current_year)

# Register Blueprints
app.register_blueprint(api)