#!/usr/bin/python3
import os
import random

from flask import Flask

app = Flask('factorioseeds')

greetings = os.environ['greetings'].split(',')


@app.route("/")
def hello():
        return "{}, World!".format(random.choice(greetings))

