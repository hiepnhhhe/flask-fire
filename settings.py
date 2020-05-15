GOOGLE_APPLICATION_CREDENTIALS = "key.json"

db_url = 'localhost:5432'
db_name = 'postgres'
db_user = 'postgres'
db_password = '1'

DB_URL = 'postgres://{DB_USER}:{DB_PASS}@/{DB_NAME}?host=/cloudsql/flask-6666:us-east1:myins'.format(
    DB_USER='postgres',
    DB_PASS='111',
    DB_NAME='postgres',
)