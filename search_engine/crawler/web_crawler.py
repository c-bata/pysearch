# -*- coding: utf-8 -*-
__author__ = 'masashi'

from search_engine import collection as col
import urllib2
import MeCab


def split_to_word(text):
    words = []
    m = MeCab.Tagger("-Ochasen")
    text = text.encode("utf-8")
    node = m.parseToNode(text)
    while node:
        words.append(node.surface)
        node = node.next
    return words


def get_page(url):
    try:
        return urllib2.urlopen(url).read()
    except:
        return ""


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url, end_pos = get_next_target(page)
        if url:
            links.append(url)
            page = page[end_pos:]
        else:
            break
    return links


def add_to_index(keyword, url):
    entry = col.find_one({'keyword': keyword})
    if entry:
        if not url in entry['url']:
            entry['url'].append(url)
            col.save(entry)
        return
    # not found, add new keyword to index
    col.insert({'keyword': keyword, 'url': [url]})


def add_page_to_index(url, content):
    for word in split_to_word(content):
        add_to_index(word, url)


def crawl_web(seed, max_depth):
    to_crawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while to_crawl and depth <= max_depth:
        page = to_crawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(, page, content)
            union(to_crawl, get_all_links(content))
            crawled.append(page)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
