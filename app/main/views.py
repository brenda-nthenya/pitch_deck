from flask import render_template,redirect,request,url_for, abort
from ..models import *
from flask_login import login_required
from . import main
from .. import db,photos

@main.route('/')
def index():

    title = 'PITCH YOUR IDEAS'
    return render_template('index.html', title = title)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
