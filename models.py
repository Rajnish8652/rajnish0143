from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo'
db = SQLAlchemy(app)
class demo(db.Model):
	serialno = db.Column(db.Integer, primary_key=True) 
	name=db.Column(db.String(20)) 
	password=db.Column(db.String(10))

def __init__(self, name, password):
	self.name = name
	self.password = password
   