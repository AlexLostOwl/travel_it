from flask import Flask, render_template
from flask_migrate import Migrate

from web_travel.models import db, User, Country, City, Place
from web_travel.crud import *


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.app_context().push()
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        # Just an Example feel fre to delete
        # save_user('Sasha', 'Umnnii_parol', 'Moi_Password')
        # save_country('Greece')
        # save_city('Smolensk', 'Germany')
        # save_place('Nice Place', 'A place description', 'Bulgaria', 'Ramensk')
        return render_template('index.html', users=get_users(), country=get_countries(), city=get_cities(),
                               place=get_places())

    return app
