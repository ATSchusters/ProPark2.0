import os

#import bcrypt
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
@app.route('/decks/', methods=['GET', 'POST'])
def show_decks():

        # if user submits a filter on the decks page
        if request.method == 'POST':
                # gather data posted from form on decks.html
                deck_filter = request.form['filter']
                deck_passtype = request.form['passtype']

                # redirect user to filtered decks page
                return redirect(url_for('display_filtered_decks', filter=deck_filter, passtype=deck_passtype))

        else:
                # retrieves all decks
                display_decks= db.session.query(Deck).all()

                # checks whether or not the user is signed in
                if session.get('user'):
                        return render_template("decks.html", decks=display_decks, user=session['user'])

                # condidtion where user is not signed in        
                else:
                        return render_template("decks.html", decks=display_decks)

# Route to show decks when users have selected a filter and pass type
@app.route('/decks/<filter>/<passtype>', methods=['GET', 'POST'])
def display_filtered_decks(filter, passtype):

        # if user submits a filter from form
        if request.method == 'POST':
                # recieve form data
                deck_filter = request.form['filter']
                deck_passtype = request.form['passtype']

                # restart display_filtered_decks with new filter
                return redirect(url_for('display_filtered_decks', filter=deck_filter, passtype=deck_passtype))
        
        else:
                # check passtype param and get decks matching it
                if passtype == "commuter":
                        filtered_decks = db.session.query(Deck).filter_by(commuter=True)
                elif passtype == "resident":
                        filtered_decks = db.session.query(Deck).filter_by(resident=True)
                elif passtype == 'faculty':
                        filtered_decks = db.session.query(Deck).filter_by(staff=True)
                else:
                        filtered_decks = db.session.query(Deck).all()
        
        # if a user is logged in, render decks.html with user and decks
        if session.get('user'):
                return render_template('decks.html', decks=filtered_decks, user=session['user'])
                
        # if no user is logged in, render decks.html with decks
        else:
                return render_template('decks.html', decks=filtered_decks)

@app.route('/schedule', methods=['GET'])
def display_schedule():
        return render_template("schedule.html")

@app.route('/settings', methods=['GET'])
def display_settings():
        return render_template("settings.html")


if __name__ == "__main__":
    app.run()