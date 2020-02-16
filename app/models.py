from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing_name = db.Column(db.String(64), index=True)
    price = db.Column(db.Integer, index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image1 = db.Column(db.String(64), index=True, unique=True)
    image2 = db.Column(db.String(64), index=True, unique=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(64), index=True, unique=True)


    def __repr__(self):
        return '<Listing {}>'.format(self.id)    

class ListingForm(FlaskForm):
    listing_name = StringField("Listing Name", validators=[DataRequired("Listing name required!")])
    price = StringField("Price per week", validators=[DataRequired("Price required!")])
    username = StringField("Username", validators=[DataRequired("Username required!")])
    image1 = StringField("Image1", validators=[DataRequired("Image1 required!")])
    image2 = StringField("Image2", validators=[DataRequired("Image2 required!")])
    submit = SubmitField("Post.")