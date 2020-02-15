from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return "lol"

@app.route('post-item')
def post():
    return "fuck"
if __name__ == '__main__':
    app.run()