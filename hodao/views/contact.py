# coding:utf8
"""

Author: ilcwd
"""
import flask
from flask import render_template

from .base import app as application
from hodao.models import contact
from .util import check_login


@application.route('/contact')
@check_login
def query_contact():
    user = flask.session['user']

    contacts = contact.query_contacts(user)
    return render_template('contacts.html', contacts=contacts)
