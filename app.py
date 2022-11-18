import os

import bcrypt
from flask import Flask, redirect, url_for, render_template, request
from database import db
from models import User as User
from models import Event as Event
from models import Deck as Deck



app = Flask(__name__)

@app.route('/')


@app.route('/login')
def login():
        return render_template("login.html")


app.run()