SET FLASK_APP=app.py
SET FLASK_ENV=development

start "" /min flask run --host=0.0.0.0 --port=80
start "" "http://localhost:80"