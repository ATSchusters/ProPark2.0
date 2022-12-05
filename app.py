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
        db.create_all()

@app.route('/')
def index():
        return render_template("index.html")


@app.route('/login', methods=['GET'])
def login():
        return render_template("login.html")

@app.route('/register', methods=['GET'])
def register():
        #need a lot more logic here
        return render_template("register.html")


#Route to display all decks with no filter to the user
@app.route('/decks/', methods=['GET'])
def show_decks():
        
        # checks whether or not the user is signed in
        if session.get('user'):
                # query and display all decks
                display_decks= db.session.query(Deck).all()
                return render_template("decks.html", decks=display_decks, user=session['user'])

        # condidtion where user is not signed in        
        else:
                # query and display all decks
                display_decks= db.session.query(Deck).all()
                return render_template("decks.html", decks=display_decks)

@app.route('/decks/<location>')
def sort_decks_by_location():
        return render_template("index.html")

@app.route('/schedule', methods=['GET'])
def display_schedule():
        return render_template("schedule.html")

@app.route('/settings', methods=['GET'])
def display_settings():
        return render_template("settings.html")


if __name__ == "__main__":
    app.run()