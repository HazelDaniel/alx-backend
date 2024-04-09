#!/usr/bin/env python3
"""module for flask app and babel"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """Configuration class for Flask application."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """gets user info if login_as provided else None"""
    user_id = request.args.get("login_as")
    if not user_id:
        return None
    for id, user in users.items():
        if id == int(user_id):
            return user
    return None


@babel.timezoneselector
def get_timezone():
    """determines the timezone to be used"""
    timezone = request.args.get("timezone")
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user.get("timezone"):
        return g.user.get("timezone")
    return Config.BABEL_DEFAULT_TIMEZONE


@app.before_request
def before_request():
    """sets g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """selecting locale based on url parameter and priority"""
    url_locale = request.args.get("locale")
    if url_locale in Config.LANGUAGES:
        return url_locale
    if g.user:
        user_local = g.user.get("locale")
        if user_local in Config.LANGUAGES:
            return user_local
    hd_locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    if hd_locale:
        return hd_locale
    return Config.BABEL_DEFAULT_LOCALE


@app.route("/")
def index():
    """the index route handler"""
    return render_template("7-index.html", user=g.user)
