#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

# Route to handle the root path "/"
@app.route("/", strict_slashes=False)
def hello():
    """
    Returns a simple greeting message.
    """
    return "Hello HBNB!"

# Route to handle the path "/hbnb"
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns "HBNB" as the response.
    """
    return "HBNB"

# Route to handle dynamic path "/c/<text>"
@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    Returns a response with "C" followed by the value of the 'text' variable.
    Replace underscores (_) in 'text' with spaces.
    """
    space_replaced = text.replace("_", " ")
    return "C {}".format(space_replaced)

# Route to handle dynamic path "/python/<text>" and default path "/python/"
@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text='is cool'):
    """
    Returns a response with "Python" followed by the value of the 'text' variable.
    Replace underscores (_) in 'text' with spaces. If 'text' is not provided, use the default value "is cool".
    """
    return f"Python {text.replace('_', ' ')}"

if __name__ == "__main__":
    # Run the Flask application on 0.0.0.0:5000 with debug mode enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
