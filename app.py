from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo
# from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail, Message

from utility import generateRandomString
import config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
# db = SQLAlchemy(app)
# mail = Mail(app)
mongo = PyMongo(app)

#
# FRONTEND ROUTES
#

#  Subscribe to poll results page
@app.route('/polls/new')
def hello():
    # This is random enough that I don't need to check for pre-existence
    # the ID before generating the page (for a toy app anyways)
    new_poll_id = generateRandomString(32)
    new_poll_url = '/polls/' + new_poll_id
    return redirect(new_poll_url)


@app.route('/polls/<id>')
def new_poll(id):
    return render_template('new_poll_subscribe.html', id=id)


# Display poll results page, but only if proper secret.
@app.route('/polls/<id>/<secret>')
def get_poll_results(id, secret):

    poll = mongo.db.polls.find_one_or_404({'_id': id})
    print poll
    if secret == poll[u'secret']:
        print poll
    return "Good"


#
# API ROUTES
#

# User subscribes to a poll,
# generate secret
# ---> send user an email
# ---> prepare row in database
@app.route('/api/polls/subscribe/<id>', methods=['POST'])
def subscribe(id):
    secret = generateRandomString(32)

    new_poll = {
        '_id': id,
        'secret': secret,
        'results': []
    }

    mongo.db.polls.insert(new_poll)

    return secret




# Recording poll results
# -->


# Retrieve results of a poll



if __name__ == '__main__':
    app.run()
