#!/usr/bin/python3
from flask import Flask

app = Flask('factorioseeds')

@app.route("/")
def hello():
        return "Hello, World!"

