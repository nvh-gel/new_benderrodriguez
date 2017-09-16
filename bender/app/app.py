""" Main application """
from flask import Flask


BENDER = Flask(__name__)


@BENDER.route('/')
def index():
    """ Homepage route """
    return "Hello World.", 200


if __name__ == "__main__":
    BENDER.run(debug=True, host='0.0.0.0')
