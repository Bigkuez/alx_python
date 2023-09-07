#!/usr/bin/python3
"""
basic flask server 
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")  # Decorator to define a route
def home():
    return "Hello HBNB!"


if __name__=="__main__":
    app.run(debug=True)
