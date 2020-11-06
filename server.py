"""
set FLASK_APP=server.py
set FLASK_ENV=development  # optional

flask run
"""

from datetime import date
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create the app and configure database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(128))


# Create database tables from models
db.create_all()

@app.route('/')
def base_view():
    var = 'Hi!'
    return var

@app.route('/events', methods=['GET', 'POST', 'DELETE'])
def events_view():
    # Create an event
    if request.method == 'POST':
        request_body = request.get_json()

        new_event = Event(
            date=date(2020, 11, request_body['day_of_month']),
            name=request_body['name']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({
            'date': new_event.date,
            'name': new_event.name
        })

    # Get list of all events
    elif request.method == 'GET':
        events = Event.query.all()

        response = []
        for event in events:
            response.append({
                'date': event.date,
                'name': event.name
            })
        return jsonify(response)

    # Show an error
    else:
        return 'I don\'t recognize that method!'
