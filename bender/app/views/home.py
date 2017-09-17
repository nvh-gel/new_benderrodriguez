""" Home page view """
from flask import Response

class Home(object):
    """ Homepage class view """
    def return_view(self):
        return Response("Hello world!", mimetype='text/plain')
