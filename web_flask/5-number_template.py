#!/usr/bin/python3
"""
A Flask web_application with_routes for_Task 5.
"""

from flask import Flask
from flask import render_template
from flask import abort

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when_accessing_the_root URL."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when_accessing_the /hbnb URL."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display 'C ' followed_by thevalue_of the_text_variable."""
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Display 'Python ' followed_by_the_value of_the_text_variable."""
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display 'n is_a number' only_if n is_an_integer."""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display_an HTML page_with 'Number: n' if n is_an_integer."""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
