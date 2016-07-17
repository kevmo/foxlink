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




`createdb foxlink`
`psql -d foxlink -f schema.sql`