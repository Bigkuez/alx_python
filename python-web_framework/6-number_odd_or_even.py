
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display a greeting message."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Route to display 'C' followed by the value of the text variable."""
    text = text.replace('_', ' ')  # Replace underscores with spaces
    return 'C {}'.format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text="is cool"):
    """Route to display 'Python' followed by the value of the text variable (default is 'is cool')."""
    text = text.replace('_', ' ')  # Replace underscores with spaces
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route to display '<n> is a number' only if n is an integer."""
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        return '', 404

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route to display an HTML page with an H1 tag containing 'Number: n' if n is an integer."""
    if isinstance(n, int):
        return f'<html><body><h1>Number: {n}</h1></body></html>'
    else:
        return '', 404

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Route to display an HTML page with an H1 tag indicating whether n is even or odd."""
    if isinstance(n, int):
        if n % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
        return f'<html><body><h1>Number: {n} is {odd_or_even}</h1></body></html>'
    else:
        return '', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
