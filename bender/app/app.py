""" Main application """
from flask import Flask
from app.views.home import Home


BENDER = Flask(__name__)


@BENDER.route('/')
def index():
    """ Homepage route """
    return Home().return_view(), 200


if __name__ == "__main__":
    BENDER.run(host='0.0.0.0')
