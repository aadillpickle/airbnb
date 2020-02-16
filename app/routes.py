from app import app
from flask import Flask, render_template, request, url_for
from flask_login import current_user, login_user
from models import User, ListingForm
from datetime import datetime
import database_methods
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/postad', methods=["POST"])
def signup():
    """ Signs a user up for an account so that they may log in """
    form = ListingForm()

    if request.method == 'POST':
        if not form.validate(): # ensure that a user enters all fields correctly
            return render_template('post-ad.html', form=form)
        else:
            username = form.username.data
            listing_name = form.listing_name.data
            price = form.price.data
            image1 = form.image1.data
            image2 = form.image2.data
            database_methods.insert_row_in_db(listing_name, datetime.time, image1, image2, username)

            return "u posted a fucking drill"