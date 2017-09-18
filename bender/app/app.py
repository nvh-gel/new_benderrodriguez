""" Main application """
from flask import Flask
from app.views.home import Home
from app.views.config import Config


BENDER = Flask(__name__)


@BENDER.route('/')
def index():
    """ Homepage route """
    return Home().return_view(), 200


@BENDER.route('/config', methods=['GET'])
def config():
    """ Config route """
    return Config().return_view(), 200


@BENDER.route('/config/json', methods=['GET'])
def config_json():
    return Config().return_json_view(), 200


if __name__ == "__main__":
    BENDER.run(debug=True, host='0.0.0.0', port=8888)
