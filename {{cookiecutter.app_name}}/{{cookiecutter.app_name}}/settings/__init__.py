# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

from __future__ import absolute_import
from __future__ import division
import os


if os.environ.get("PROJECT_ENV") == 'prod':
    from .prod import ProdConfig as settings
else:
    from .dev import DevConfig as settings
