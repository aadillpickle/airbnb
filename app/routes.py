from app import app
from flask import Flask, render_template, request, url_for


@app.route('/')
def index():
    return render_template('index.html')