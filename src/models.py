from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    def _repr_(self):
        return '<User %r>' % self.email #self.X tiene que ser uno de ,los identificadores del User que me permita diferenciarlo de los demás
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.String(50), unique=True, nullable=False)
    hair_color = db.Column(db.String(50), unique=True, nullable=False)
    eye_color = db.Column(db.String(50), unique=True, nullable=False)
    
    def _repr_(self):
        return '<Characters %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }