from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email =  db.Column(db.String(100))
    password = db.Column(db.String(100))
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bottles = db.Column(db.Integer)
    shower = db.Column(db.Integer)
    recycle = db.Column(db.String(10))
    transport = db.Column(db.String(20))
    computer = db.Column(db.String(20))
    appliances = db.Column(db.String(20))
    lights = db.Column(db.String(20))
    air = db.Column(db.String(10))
    meat = db.Column(db.String(10))

    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    