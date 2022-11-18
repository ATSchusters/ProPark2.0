from database import db

class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    password = db.Column('password', db.String(36))
    first_name = db.Column('first_name', db.String(20))
    last_name = db.Column('last_name', db.String(20))
    email = db.Column('email', db.String(30))

    def __init__(self, password, first_name, last_name, email):
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
class Event(db.Model):
    id = db.Column ('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer)
    location = db.Column('location', db.String(50))
    time = db.Column('time', db.Integer)
    recurring = db.Column('recurring',db.String(10))

    def __init__(self, location, user_id, time, recurring):
        self.location = location
        self.user_id = user_id
        self.time = time
        self.recurring = recurring

class Deck(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(30))
    coord_x = db.Column('coord_x', db.Float)
    coord_y = db.Column('coord_y', db.Float)
    passtype = db.Column('passtype', db.String(10))

    def __init__(self, name, coord_x, coord_y, passtype):
        self.name = name 
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.passtype = passtype