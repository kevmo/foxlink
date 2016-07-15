from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from utility import generateRandomString
import config


app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)

db = SQLAlchemy(app)


#
# FRONTEND ROUTES
#

#  Subscribe to poll results page
@app.route('/polls/new')
def hello():
    new_poll_id = generateRandomString(32)
    new_poll_url = '/polls/' + new_poll_id
    return redirect(new_poll_url)


@app.route('/polls/<id>')
def new_poll(id):
    return render_template('new_poll_subscribe.html', id=id)


# Display poll results page, but only if proper secret.
@app.route('/polls/<id>/<secret>')
def what():
    return


#
# API ROUTES
#

# User subscribes to a poll,
# generate secret
# ---> send user an email
# ---> prepare row in database
@app.route('/api/polls/subscribe/<id>', methods=['POST'])
def subscribe(id):
    return "success"


# Recording poll results
# -->


# Retrieve results of a poll



if __name__ == '__main__':
    app.run()
