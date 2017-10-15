#!/usr/bin/env python3
""" Main application """
from flask import Flask, request
from app.views.home import Home
from app.views.config import Config
from app.views.opsgenie import Opsgenie
from app.views.classificator import Classificator
from app.controllers.mt_io import print_stderr


BENDER = Flask(__name__)


@BENDER.route('/')
def index():
    """ Homepage route """
    print_stderr('home route')
    return Home().return_view(), 200


@BENDER.route('/config', methods=['GET'])
def config():
    """ Config route """
    return Config().return_view(), 200


@BENDER.route('/config/json', methods=['GET'])
def config_json():
    """ Return config in json """
    return Config().return_json_view(), 200


@BENDER.route('/opsgenie', methods=['POST'])
def send_to_opsgenie():
    """ Allow posted payload from Opsgenie """
    payload = request.get_json(force=True)
    return Opsgenie().return_view(payload=payload)


@BENDER.route('/classify', methods=['GET'])
def get_classfication_json():
    """ Check classification from given alert and return as json """
    # issue = request.args.get('issue') if 'issue' in request.args else None
    # is_json = True if 'json' in request.args else False
    issue = request.args.get('issue')
    is_json = True if 'json' in request.args else False
    if issue:
        if is_json:
            return Classificator().return_json_view(issue=issue)
        else:
            return Classificator().return_view(issue=issue)
    else:
        return Classificator().return_view()


if __name__ == "__main__":
    BENDER.run(debug=True, host='0.0.0.0', port=8888)
