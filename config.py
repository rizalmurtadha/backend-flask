import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://udfhxpwg:7wv8Sbg4BbcpNvV8VMwjr6qhyxke9Czm@rosie.db.elephantsql.com/udfhxpwg'
    SQLALCHEMY_TRACK_MODIFICATIONS = False