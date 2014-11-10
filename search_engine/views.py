# -*- coding: utf-8 -*-
__author__ = 'masashi'

from search_engine import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    """Return index.html
    """
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            query = ['http://google.com', 'http://amazon.co.jp']
            return render_template('index.html', urls=query, keyword=keyword)
    return render_template('index.html')
