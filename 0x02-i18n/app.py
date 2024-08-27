#!/usr/bin/env python3
"""
Display the current time
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """
    configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/')
def home():
    """
    home method
    """
    g.time = format_datetime()
    return render_template('index.html')

def get_user():
    """
    Function that returns a user dictionary or \
            None if the ID cannot be found or if login_as was not passed
    """
    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None

@app.before_request
def before_request():
    """
    Function that execute before all other functions \
            uses get_user to find a user if any, and set it as a global
    """
    g.user = get_user()

@babel.timezoneselector
def get_timezone():
    """
    Finds the timezone of a user
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']

    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        print(pytz.exceptions.UnknownTimeZoneError)
        return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.localeselector
def get_locale():
    """
    Function that determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run(debug=True)
