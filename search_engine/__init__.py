# -*- coding: utf-8 -*-
__author__ = 'masashi'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from search_engine import views