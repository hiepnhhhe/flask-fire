from flask import Flask
from my_page.extensions import bcrypt, db, jwt, cors, migrate, ma, api
from .settings import ProdConfig
from .user.views import blueprint as user_print
from .elemental.views import blueprint as element_print

def create_app(config_object=ProdConfig):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    api.init_app(user_print)


def register_blueprints(app):
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(user_print, origins=origins)

    app.register_blueprint(user_print, url_prefix='/api/1')
    app.register_blueprint(element_print)