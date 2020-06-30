import os

class Config(object):
    SECRET_KEY  = os.urandom(12)

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_DATABASE_USER = 'Admin'
    MYSQL_DATABASE_PASSWORD = 'qwerty0000'
    MYSQL_DATABASE_BD = 'blocknote'
    MYSQL_DATABASE_HOST = 'localhost'