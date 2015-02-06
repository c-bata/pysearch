# -*- coding: utf-8 -*-

from search_engine import app, collection as col
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    """Return index.html
    """
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            return render_template(
                'index.html',
                query=col.find_one({'keyword': keyword}),
                keyword=keyword)
    return render_template('index.html')
