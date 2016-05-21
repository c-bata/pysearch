from urllib.parse import urlparse
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')

# DB settings
MONGO_URL = app.config['MONGO_URL']
client = MongoClient(MONGO_URL)
db = client[urlparse(MONGO_URL).path[1:]]
col = db["Index"]


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
