class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '4ds5a456sa4g87h8ts465s4j5h4k5u'
    FLASK_APP = 'app:wsgi.py'
    JWT_DEFAULT_REALM = 'Login Required'