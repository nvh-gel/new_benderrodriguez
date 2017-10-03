# """ Config page view """
""" Config page view """
from flask import render_template, jsonify
from app.controllers.mt_config_handler import MTConfigHandler


class Config(object):
    """ Homepage class view """
    def return_view(self):
        """ Return config page """
        config = MTConfigHandler().get_config()
        return render_template('config.html', name='Bender', config=config)

    def return_json_view(self):
        """ Return config in json format """
        return jsonify(MTConfigHandler().get_config())
