# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

from .base import  Config


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing
