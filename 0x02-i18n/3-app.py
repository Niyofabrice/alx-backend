#!/usr/bin/env python3
"""
Parametrize templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

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
    return render_template('3-index.html')

@babel.localeselector
def get_locale():
    """
    Function that determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run(debug=True)
