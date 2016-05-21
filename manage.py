import argparse
__author__ = 'c-bata'


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Runner")
    parser.add_argument('action', type=str, nargs=None, help="Select target 'crawler' or 'webpage'?")
    args = parser.parse_args()

    if args.action == 'crawler':
        from web_crawler.crawler import crawl_web
        crawl_web('http://docs.sphinx-users.jp/contents.html', 2)
    elif args.action == 'webpage':
        from search_engine import app
        app.run(debug=True, port=9000)
    else:
        raise ValueError('Please select "crawler" or "webpage".')
