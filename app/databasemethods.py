import sqlite3
import os
from werkzeug.security import generate_password_hash
from uuid import uuid4

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../app.db")


def insert_row_in_db(listing_name, time, image1, username):
    """ Creates a row in chat.sqlite's users table """
    uid = uuid4().hex
    row_data = (uid, listing_name, time, image1, username)

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO users (uid, listing_name, time, image1, username) VALUES (?, ?, ?, ?, ?);''', row_data)