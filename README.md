Requirements:
* Python
* [VirtualEnvWrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)
* MongoDB - `brew install mongodb`

1) Set up environment & install required Python packages.
`mkvirtualenv foxlink`
`workon foxlink`
`pip install -r requirements.txt`

2) Start a MongoDB database
`brew services start mongodb`

3) Launch from home dir.
`python app.py`

4) Start
Begin a new poll: http://localhost:5000/polls/new.  If you
subscribe, the page will give you directions for API poll 
result recording and viewing said poll results.

