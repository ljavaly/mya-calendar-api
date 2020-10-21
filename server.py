from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the app and configure database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/calendar.db'
db = SQLAlchemy(app)


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)


# Create database tables from models
db.create_all()

@app.route('/')
def base_view():
    return 'Hi!'
