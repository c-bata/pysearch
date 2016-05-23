import requests
from urllib.parse import urlparse

from pymongo import MongoClient
from janome.tokenizer import Tokenizer
from bs4 import BeautifulSoup

from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client[urlparse(MONGO_URL).path[1:]]
col = db["Index"]


def _split_to_word(text):
    """Japanese morphological analysis with janome.
    Splitting text and creating words list.
    """
    t = Tokenizer()
    return [token.surface for token in t.tokenize(text)]


def _get_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text


def _extract_url_links(html):
    """extract url links

    >>> _extract_url_links('aa<a href="link1">link1</a>bb<a href="link2">link2</a>cc')
    ['link1', 'link2']
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all('a')


def add_to_index(keyword, url):
    entry = col.find_one({'keyword': keyword})
    if entry:
        if url not in entry['url']:
            entry['url'].append(url)
            col.save(entry)
        return
    # not found, add new keyword to index
    col.insert({'keyword': keyword, 'url': [url]})


def add_page_to_index(url, html):
    body_soup = BeautifulSoup(html, "html.parser").find('body')
    for child_tag in body_soup.findChildren():
        if child_tag.name == 'script':
            continue
        child_text = child_tag.text
        for line in child_text.split('\n'):
            line = line.rstrip().lstrip()
            for word in _split_to_word(line):
                add_to_index(word, url)


def crawl_web(seed, max_depth):
    to_crawl = {seed}
    crawled = []
    next_depth = []
    depth = 0
    while to_crawl and depth <= max_depth:
        page_url = to_crawl.pop()
        if page_url not in crawled:
            html = _get_page(page_url)
            add_page_to_index(page_url, html)
            to_crawl = to_crawl.union(_extract_url_links(html))
            crawled.append(page_url)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
