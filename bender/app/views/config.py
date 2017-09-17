# """ Config page view """
""" Home page view """
from flask import render_template

class Config(object):
    """ Homepage class view """
    def return_view(self):
        return render_template('config.html', name='Bender')
