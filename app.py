import os

import bcrypt
from flask import Flask, redirect, url_for, render_template, request, session
from database import db
from models import User as User
from models import Event as Event
from models import Deck as Deck

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///propark_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
        db.create_all

@app.route('/')


@app.route('/login', methods=['GET'])
def login():
        return render_template("login.html")


#Route to display all decks with no filter to the user
@app.route('/decks/', methods=['GET'])
def show_decks():

        all_decks= db.session.query(Deck).all()

        if session.get('user'):
        



if __name__ == "__main__":
    app.run()