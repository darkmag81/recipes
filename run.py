from os.path import exists
from functools import wraps
from flask import Flask, redirect, jsonify, render_template, request, flash, url_for
import os
import json
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'superpassword1'
app.secret_key = 'some_secret'


@app.route("/")
def hello():
    return render_template('index.html', page_title="Recipes Home")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            debug=True)
