# -*- coding: utf-8 -*-

from web_crawler import collection as col
import urllib2
import MeCab


def split_to_word(text):
    """
    MeCabを使って日本語を形態素解析
    単語に切り分け、リストをつくる
    """
    words = []
    m = MeCab.Tagger("-Ochasen")
    text = unicode(text, "utf-8")
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
    """
    リストを結合．重複していれば追加しない

    >>> a, b = ['a', 'b', 'c'], ['b', 'c', 'd']
    >>> union(a,b)
    >>> print a
    ['a', 'b', 'c', 'd']
    """
    for e in b:
        if e not in a:
            a.append(e)


def get_next_target(page):
    """
    文字列に変換したWeb文書からURLリンクを抽出

    >>> ('link1', 16) == get_next_target('aa<a href="link1">link</a>bbcc')
    True
    >>> (None, 0) == get_next_target('aabbcc')
    True
    """
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    """
    文字列に変換したWeb文書内のURLリンクを全て抽出してリストに格納．

    >>> ['link1', 'link2'] == get_all_links('aa<a href="link1">link1</a>bb<a href="link2">link2</a>cc')
    True
    """
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
        page = to_crawl.pop(0)
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(page, content)
            union(to_crawl, get_all_links(content))
            crawled.append(page)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
