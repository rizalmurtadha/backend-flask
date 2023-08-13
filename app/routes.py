from flask import render_template
from app import app
from app.models import Item

@app.route('/')
def index():
    return "Hello, world!"
    # users = User.query.all()
    # return render_template('index.html', users=users)