import os

DB_URL = 'postgres://{DB_USER}:{DB_PASS}@/{DB_NAME}?host=/cloudsql/flask-6666:us-east1:myins'.format(
    DB_USER='postgres',
    DB_PASS='111',
    DB_NAME='postgres',
)

db_url = 'localhost:5432'
db_name = 'postgres'
db_user = 'postgres'
db_password = '1'

class Config(object):
    SECRET_KEY = 'haisefrost'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:4200',
        'http://localhost:4200',
        'http://0.0.0.0:8000',
        'http://localhost:8000',
    ],
    JWT_BLACKLIST_ENABLED = True,
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_DATABASE_URI = f'postgres://{db_user}:{db_password}@{db_url}/{db_name}'