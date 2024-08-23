from app import app
import config

if __name__ == '__main__':
  try:
    if config.FLASK_ENV == 'production':
      from waitress import serve
      serve(app, host="0.0.0.0", port=8080)
    else:
      app.run(debug=True)
  finally:
    print('Service closed')
