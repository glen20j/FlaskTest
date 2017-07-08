import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:pass@msomepostgrelutlAFL_Schedule'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'Andy'
