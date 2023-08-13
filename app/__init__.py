from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Item
with app.app_context():
    db.create_all()

    db.session.commit()
    
    item = Item.query.all()
    print(item)


from app import models, resources