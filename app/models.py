from app import db

class Episode(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    date =db.Column ( db.String)
    number= db.Column (db.Integer)
    appearances =db.relationship ('Appearance', backref='episode', cascade='all, delete')

class Guest(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    occupation = db.Column(db.String)
    appearances =db.relationship('Appearance',backref='guest',cascade='all, delete')

class Appearance(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    guest_id= db.Column(db.Integer, db.ForeignKey('guest.id'))