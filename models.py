Contents:
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Role(db.Model):id = db.Column(db.Integer, primary_key=True)name = db.Column(db.String(64), unique=True, nullable=False)

class User(UserMixin, db.Model):id = db.Column(db.Integer, primary_key=True)phone = db.Column(db.String(32), unique=True, nullable=False)name = db.Column(db.String(128), nullable=False)password = db.Column(db.String(128), nullable=False)  # plaintext for demo onlyrole_id = db.Column(db.Integer, db.ForeignKey('role.id'))
role = db.relationship('Role')

class Contribution(db.Model):id = db.Column(db.Integer, primary_key=True)member_id = db.Column(db.Integer, db.ForeignKey('user.id'))amount = db.Column(db.Float, nullable=False)date = db.Column(db.DateTime, default=datetime.utcnow)note = db.Column(db.String(256))member = db.relationship('User')

class Transaction(db.Model):id = db.Column(db.Integer, primary_key=True)description = db.Column(db.String(256))amount = db.Column(db.Float, nullable=False)date = db.Column(db.DateTime, default=datetime.utcnow)
