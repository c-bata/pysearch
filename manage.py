# -*- coding: utf-8 -*-
import sys
__author__ = 'c-bata'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments.")
        sys.exit(1)
    elif sys.argv[1] == 'crawler':
        from web_crawler import crawl_web
        crawl_web('http://docs.sphinx-users.jp/contents.html', 2)
    elif sys.argv[1] == 'web':
        from search_engine import app
        app.run(debug=True)
    else:
        print('"{}" is unknown option'.format(sys.argv[1]))
        sys.exit(1)

