#!/usr/bin/env python3
"""setting up a basic flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """the index route handler"""
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
