#!/usr/bin/env python3
"""force locale based on url parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """the class for the i18n configuration"""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """selecting locale based on best match"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """the index route handler"""
    return render_template("4-index.html")

# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
