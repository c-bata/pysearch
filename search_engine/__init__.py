# -*- coding: utf-8 -*-

from flask import Flask
from pymongo import MongoClient
from urlparse import urlparse
from search_engine import views

app = Flask(__name__)
app.config.from_object('config')

# DB settings
MONGO_URL = app.config['MONGO_URL']
client = MongoClient(MONGO_URL)
db = client[urlparse(MONGO_URL).path[1:]]
collection = db["Index"]
