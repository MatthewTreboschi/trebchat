# models.py
import flask_sqlalchemy
from app import db


class Trebchat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String())
    names = db.Column(db.String())
    
    def __init__(self, a, b):
        self.message = a
        self.names = b
        
    def __repr__(self):
        return '<Trebchat message: %s>' % self.message
        
class activeusers(db.Model):
    sid = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String())
    
    def __init__(self, a, b):
        self.sid = a
        self.username = b
        
    def __repr__(self):
        return '<Trebchat message: %s>' % self.message
        

