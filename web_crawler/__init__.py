# -*- coding: utf-8 -*-
__author__ = 'masashi'

from config import MONGO_URL
from pymongo import MongoClient
from urlparse import urlparse

client = MongoClient(MONGO_URL)
db = client[urlparse(MONGO_URL).path[1:]]
collection = db["Index"]

from crawler import crawl_web