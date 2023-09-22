#!/usr/bin/python3
"""
A Flask_web application_with two_routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when_accessing_the root URL."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when_accessing_the /hbnb URL."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
