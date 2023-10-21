#!/usr/bin/python3
"""
A simple_Flask web_application.
"""
# Import_necessary_modules
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define_a_route that_serves content_for "/airbnb-onepage/"
@app.route('/airbnb-onepage/', methods=['GET'])
def hello_airbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    # Run_the Flask_application_on port_5000
    app.run(host="0.0.0.0", port=5000)
