from flask import request
from flask_babel import Babel


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app = Flask(__name__)


babel = Babel(app, locale_selector=get_locale)
