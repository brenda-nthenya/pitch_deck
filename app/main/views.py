from flask import render_template,redirect,request,url_for, abort

from flask_login import login_required
from . import main

@main.route('/')
def index():

    title = 'PITCH YOUR IDEAS'
    return render_template('index.html', title = title)


