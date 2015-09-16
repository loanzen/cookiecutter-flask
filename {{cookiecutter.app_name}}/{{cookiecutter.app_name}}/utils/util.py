# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from __future__ import absolute_import
from __future__ import division
import collections
import importlib
import re

from flask import flash
from {{cookiecutter.app_name}} import compat


def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                  .format(getattr(form, field).label.text, error), category)


def import_class(cls_path):
    if not isinstance(cls_path, compat.string_types):
        return cls_path
    #cls is a module path to string
    if '.' in cls_path:
            # Try to import.
            module_bits = cls_path.split('.')
            module_path, class_name = '.'.join(module_bits[:-1]), module_bits[-1]
            module = importlib.import_module(module_path)
    else:
        # We've got a bare class name here, which won't work (No AppCache
        # to rely on). Try to throw a useful error.
        raise ImportError("Rquires a Python-style path (<module.module.Class>) "
                          "to load given cls. Only given '%s'." % cls_path)

    cls = getattr(module, class_name, None)

    if cls is None:
        raise ImportError("Module '%s' does not appear to have a "
                          "class called '%s'." % (module_path, class_name))

    return cls


def convert_value_to_python(value):
    """
    Turn the string ``value`` into a python object.
    """
    # Simple values
    if value in ['true', 'True', True]:
        value = True
    elif value in ['false', 'False', False]:
        value = False
    elif value in ('nil', 'none', 'None', None):
        value = None

    return value


def recursive_update(d, u):
    for k, v in u.iteritems():
        if isinstance(d, collections.Mapping):
            if isinstance(v, collections.Mapping):
                r = recursive_update(d.get(k, {}), v)
                d[k] = r
            else:
                d[k] = u[k]
        else:
            d = {k: u[k]}
    return d


def camelcase_undescore_converter(value):
    return re.sub('([A-Z])',
                  lambda m: "_" + m.group(1).lower(), value).lstrip('_')
