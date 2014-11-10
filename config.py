# -*- coding: utf-8 -*-
__author__ = 'masashi'

import os

# application settings
MONGO_URL = 'please input mongodb uri'

# Generate a random secret key
SECRET_KEY = os.urandom(24)
CSRF_ENABLED = True