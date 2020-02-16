# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config(object):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# from flask import Flask, render_template, request, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # l = Listing(id=0,first_name="aryan",last_name="misra",listing_name="drill",city="toronto",province="ontario",country="canada",postal_code="no u",price=22)
# # print(l)


# if __name__ == "__main__":
#     app.run(debug=True)
from app import app, db
from app.models import User, Listing


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Listing': Listing}