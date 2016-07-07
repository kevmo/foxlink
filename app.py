from flask import Flask
app = Flask(__name__)


#
# FRONTEND ROUTES
#

#  Subscribe to poll results page
@app.route('/')
def hello():
    return "Hello World!"


# Display poll results page, but only if proper secret.




#
# API ROUTES
#

# User subscribes to a poll,
# ---> send user an email
# ---> prepare row in database


# Recording poll results
# -->


# Retrieve results of a poll



if __name__ == '__main__':
    app.run()
