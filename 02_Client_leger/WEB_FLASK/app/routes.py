from app import app
from flask import render_template


@app.route('/') # decorators
@app.route('/index')
def index():
    return render_template ('home.html')
    return strResult


@app.route('/list')
def list():
    return render_template ('list_bdd.html')
    return strResult




