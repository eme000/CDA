from app import app
from flask import render_template


@app.route('/') # decorators
@app.route('/index')
def index():
    return render_template ('home.html')
    return strResult


@app.route('/oui')
def oui():
    strResult = 'non'
    return render_template ('home.html')
    return strResult




