#!/usr/bin/env python3
"""task-1: setting up a basic flask application"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """the class for the i18n configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index():
    """the route handler for the index route"""
    return render_template("1-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
