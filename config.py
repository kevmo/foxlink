import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DATABASE_URL = "postgresql://localhost/foxlink"
    DEVELOPMENT = True
    DEBUG = True
