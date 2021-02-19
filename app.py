#!/usr/bin/python3
import os
import random

from flask import Flask, render_template

app = Flask('factorioseeds')

if 'greetings' in os.environ:
    greetings = os.environ['greetings'].split(',')
else:
    greetings = ['Hello', 'Hi', 'Boop']

@app.route("/")
def hello():
        return render_template('index.html', greeting=random.choice(greetings))

