from app import app
from flask import render_template


@app.route('/') # decorators
@app.route('/index')
def index():
    strResult = 'Bruz!'
    return strResult


@app.route('/oui')
def oui():
    strResult = 'non'
    return strResult




