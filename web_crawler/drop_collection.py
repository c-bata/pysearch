# -*- coding: utf-8 -*-
__author__ = 'masashi'

from web_crawler import collection as col


def drop_collection():
    col.drop()

if __name__ == '__main__':
    drop_collection()
