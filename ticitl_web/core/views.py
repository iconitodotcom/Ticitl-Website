# ticitl_web/core/views.py
#
# Description: Core section has web view and platform login view
#
# Change History:
# Issue(opt)   Modifier            MM/DD/YYYY  Description
# ------       ------------------  ----------  ----------------------------------
#  n/a         Julio Conchas       05/03/2025  Initial include of change history header.

from flask import render_template, request, Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('core/index.html')

@core.route('/login')
def login():
    return render_template('core/login.html')

@core.route('/signup/<plan>')
def signup(plan):
    return render_template('core/signup.html')