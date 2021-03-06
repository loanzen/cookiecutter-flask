#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask_script import Manager, Shell, Server
from flask_script.commands import Clean, ShowUrls
from flask_migrate import MigrateCommand

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import settings

app = create_app(settings)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app}


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


manager.add_command('server', Server())
shell_banner = """
Welcome to your Flask CLI environment.
The following variables are available to use:
app           -> Your Flask app instance.
"""
manager.add_command('shell', Shell(banner=shell_banner,
                                   make_context=_make_context))

manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == '__main__':
    manager.run()
