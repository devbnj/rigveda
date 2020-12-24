# main.py

from flask import Blueprint, render_template, json, session
from flask_login import login_required, current_user
import os
from flask import current_app as app

pagecount = 1
maxpage = 35
main = Blueprint('main', __name__)

'''
@main.route('/')
def index():
    return render_template('index.html')
'''

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile/')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, rigved=current_user.rigved)

# def
def commonClass(pg):
    if pg == 0:
        pg = 1
    if 'page' in session:
        pg = session['page']
    filename = os.path.join(app.static_folder, ('class%d.json') % pg)
    actdata = {}
    with open(filename) as scriptures_file:
        tdata = json.load(scriptures_file)
        # print (tdata)
        actdata = tdata["data"]
    return render_template('class.html', name=current_user.name, page=pg, posts=actdata)
# end def

@main.route('/class/')
@login_required
def rigclass():
    global pagecount
    return commonClass(pagecount)

@main.route('/prevclass/')
@login_required
def prevclass():
    global pagecount
    if 'page' in session:
        pg = session['page']
    else:
        pg = pagecount
        session['page'] = pg
    # page decrement
    pg = pg - 1
    if pg < 1:
        pg = 1
    session['page'] = pg
    return commonClass(pg)

@main.route('/nextclass/')
@login_required
def nextclass():
    global pagecount
    if 'page' in session:
        pg = session['page']
    else:
        pg = pagecount
        session['page'] = pg
    if pg < maxpage:
        pg = pg + 1
    session['page'] = pg
    return commonClass(pg)

@main.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500