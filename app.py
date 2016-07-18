import json

from flask import Flask, redirect, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps

import config
from utility import generateRandomString


# Configuration
app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
mongo = PyMongo(app)

#
# FRONTEND ROUTES
#

@app.route('/polls/new')
def generate_new_poll():
    # This is random enough that I don't need to check for pre-existence
    # of the ID before generating the page (for a toy app anyways).
    new_poll_id = generateRandomString(32)
    new_poll_url = '/polls/' + new_poll_id
    return redirect(new_poll_url)


@app.route('/polls/<id>')
def new_poll(id):
    return render_template('new_poll_subscribe.html', id=id)


# Display poll results page, but only if proper secret.
@app.route('/polls/<id>/<secret>')
def view_poll_results(id, secret):

    poll = mongo.db.polls.find_one_or_404({'_id': id})
    # Checking secret --> would be better done as a decorator
    if secret == poll[u'secret']:
        return render_template('poll_results.html', id=id), 200
    else:
        return "You don't belong here.", 401


#
# API ROUTES
#


# Skipping sending user an email because of time constraints, would otherwise use sendgrid.
@app.route('/api/polls/subscribe/<id>', methods=['POST'])
def subscribe(id):
    secret = generateRandomString(32)

    new_poll = {
        '_id': id,
        'secret': secret,
        'results': []
    }

    mongo.db.polls.insert(new_poll)

    return secret, 201


# Recording poll results.  Including GET in allowable methods for ease of testing
@app.route('/api/polls/<id>', methods=['GET', 'POST'])
def record_poll_results(id):
    existing_poll = mongo.db.polls.find_one_or_404({'_id': id})

    new_results = {}
    for key in request.args:
        new_results[key] = request.args[key]
        existing_poll[u'results'].append(new_results)

    # This is the worst way in the world to update, but... You said don't spend more than a few hours on this.
    updated_poll = mongo.db.polls.replace_one(
        {'_id': existing_poll[u'_id']},
        existing_poll
    )

    return "Good"


# not explicitly hidden behind a secret - should be in production app
@app.route('/api/polls/<id>/results')
def get_poll_results(id):
    poll = mongo.db.polls.find_one_or_404({'_id': id})
    poll = json.dumps(poll[u'results'])
    return jsonify(poll=poll)


if __name__ == '__main__':
    app.run()
