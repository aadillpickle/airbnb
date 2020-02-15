from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
# from bson.json import util
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'airbnb'
app.config['MONGO_URI'] = 'mongodb+srv://aryanmisra:Pirate%4012345@cluster0-4r7fx.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

# return Response(
#     json_util.dumps({'page' : make_public_page(page)}),
#     mimetype='application/json'
# )
result = mongo.db.test.find()
print(result)



@app.route('/')
def home():

    return Response(
    json_util.dumps({'page' : make_public_page(page)}),
    mimetype='application/json'
)

@app.route('/post-item')
def post():
    return "fuck"

@app.route('/index')
def index():
    emp_list = mongo.db.employee_entry.find()
    return render_template('index-2.html', emp_list = emp_list)

if __name__ == "__main__":
    app.run(debug=True)