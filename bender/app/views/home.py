""" Home page view """
from flask import render_template

class Home(object):
    """ Homepage class view """
    def return_view(self):
        return render_template('index.html', name='Bender')
