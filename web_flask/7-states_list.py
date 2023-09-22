#!/usr/bin/python3
"""Import Flask_to_run the_web_app."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def display_states():
    """Route_to render_the states_list HTML page_and display_States."""
    states = storage.all()  # Fetch all objects from the storage
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_db_session(exception):
    """Method_to_remove the_current SQLAlchemy Session_after each_request."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
