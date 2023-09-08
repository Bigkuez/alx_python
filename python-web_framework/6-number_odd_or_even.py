#!/usr/bin/python3
"""
basic flask server 
"""
from flask import Flask , render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    text = text.replace('_', ' ')  # Replace underscores with spaces
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text="is cool"):
    text = text.replace('_', ' ')  # Replace underscores with spaces
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        return '', 404
    
    
    
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return f'<html><body><h1>Number: {n}</h1></body></html>'
    else:
        return '', 404
    
    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
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
