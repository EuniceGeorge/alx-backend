from flask import request
from flask_babel import Babel


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app = Flask(__name__)

class Config():
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app, locale_selector=get_locale)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """ get locale language code from request accepted languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name_ = '__main__':
    app.run(debug=True)
