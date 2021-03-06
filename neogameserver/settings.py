import tempfile
import os
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'REPLACE ME'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./database.db'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHURI')
    MONGODB_SETTINGS = {
        "db": "neogameserver",
        "host": "mongodb://localhost/neogameserver"
    }

    DEBUG_TB_PANELS = ['flask.ext.mongoengine.panels.MongoDebugPanel']

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True


class TestConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
