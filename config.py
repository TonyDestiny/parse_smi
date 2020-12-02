import os
WORK_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(WORK_DIR, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEYS = False