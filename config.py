import os
import mysql.connector as ms

class Config(object):
    SECRET_KEY  = 'my_secret_key_di_que_eres_puto'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'Admin'
    MYSQL_DATABASE_PASSWORD = 'qwerty0000'
    MYSQL_DATABASE_DB = 'blocknote'
