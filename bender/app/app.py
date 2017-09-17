""" Main application """
from flask import Flask
from views.home import Home
from views.config import Config


BENDER = Flask(__name__)


@BENDER.route('/')
def index():
    """ Homepage route """
    return Home().return_view(), 200


@BENDER.route('/config')
def config():
    """ Config route """
    return Config().return_view(), 200


if __name__ == "__main__":
    BENDER.run(host='0.0.0.0', port=8888)
