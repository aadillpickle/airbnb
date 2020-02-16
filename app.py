from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask import g
# from bson.json import util
import os

app = Flask(__name__)


@app.route('/post-item')
def post():
    return "fuck"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)