SET FLASK_APP=app.py
SET FLASK_ENV=development

start "" /min flask run --host=0.0.0.0
start "" "http://localhost:"