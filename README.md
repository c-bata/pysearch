# Pythonで作る検索エンジン

## Description

![スクリーンショット 2014-11-11 22.49.07.png](https://qiita-image-store.s3.amazonaws.com/0/29989/786c36ad-4de7-43a7-75a0-98c82e412fa3.png "スクリーンショット 2014-11-11 22.49.07.png")

勉強用に作った検索エンジン。やったことは以下のとおり。

- Webクローラの構築
- Mecabで日本語の形態素解析
- 検索エンジンの構築
- データをMongoDBに格納
- FlaskでWebアプリ作成

詳しくはブログのほうに書きます([c-bata web](http://nwpct1.hatenablog.com/entry/python-search-engine))。

## Requirements

- Python 2.7
- pip
- MeCab


## Setup

1. Clone repository

    ```
    $ git clone git@github.com:mejiro/SearchEngine.git
    ```
    
1. Install Mecab 

    ```
    $ # MeCab
    $ brew install mecab mecab-ipadic
    $ # Python binding
    $ wget https://mecab.googlecode.com/files/mecab-python-0.996.tar.gz
    $ workon search_engine
    $ pip install mecab-python-0.996.tar.gz # これでいれれる!
    $ rm mecab-python-0.996.tar.gz
    ```
    
    ###### 参考
    
    [Homebrew + Virtualenv 環境でMeCabのインストール : さりんじゃーのプログラミング日記](http://salinger.github.io/blog/2013/01/17/1/)

1. Install python packages

    ```
    $ cd SearchEngine
    $ pip install -r requirements.txt
    ```

1. MongoDB settings

    Please rewrite MONGO_URL in settings.py
    
1. Run

    ```
    $ python run-crawler.py # build a index
    $ python run-webapp.py # access to http://127.0.0.1:5000
    ```
