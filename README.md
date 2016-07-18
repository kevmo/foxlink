Requirements:
* Python 2
* [VirtualEnvWrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)
* MongoDB - `brew install mongodb`

0) Set up environment & install required Python packages.
`mkvirtualenv foxlink`
`workon foxlink`
`pip install -r requirements.txt`

1) Start a MongoDB database
`brew services start mongodb`

2) Install front-end packages
`bower install`

3) Launch from home dir.
`python app.py`

4) Start
Begin a new poll: http://localhost:5000/polls/new.  If you
subscribe, the page will give you directions for API poll 
result recording and viewing said poll results.

Issues/potential improvements:
* Needs more/better error handling, particularly in API routes.
* Email requirement unmet.
* Using unminified static assets.
* Not mobile-friendly.
* Security could be drastically improved.
* Add PEP docstrings to all Python route functions, including explanations of paths/parameters.