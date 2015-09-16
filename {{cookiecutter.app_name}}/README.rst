===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export {{cookiecutter.app_name | upper}}_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.app_name }}
    cd {{cookiecutter.app_name}}
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen.

Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``.


Running Tests
-------------

To run all tests, run ::

    python manage.py test

