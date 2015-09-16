# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""

import sys
import cdecimal

sys.modules["decimal"] = cdecimal

from flask import Flask, render_template

from {{cookiecutter.app_name}}.settings import settings
from {{cookiecutter.app_name}}.extensions import (
    bcrypt,
    cache,
    login_manager,
    debug_toolbar,
)


def create_app(config_object=settings):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    cache.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    return None


def register_blueprints(app):
    pass


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
