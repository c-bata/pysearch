# Pythonで作る検索エンジン

## Description

勉強用に作った検索エンジン。やったことは以下のとおり。

- Webクローラの構築
- Mecabで日本語の形態素解析
- 検索エンジンの構築
- データをMongoDBに格納
- FlaskでWebアプリ作成

詳しくはブログのほうに書きます([Programming Log](http://nwpct1.hatenablog.com))。

## Requirements

- Python 2.7
- pip
- Mecab

## Setup

1. Clone repository

    ```
    $ git clone git@github.com:mejiro/SearchEngine.git
    ```
    
1. Install Mecab 

    ```
    $ # Mecab
    $ brew install mecab mecab-ipadic
    $ # Python binding
    $ wget https://mecab.googlecode.com/files/mecab-python-0.996.tar.gz
    $ workon search_engine
    $ pip install mecab-python-0.996.tar.gz # これでいれれる!
    $ rm mecab-python-0.996.tar.gz
    ```
    
    ###### 参考
    
    [Homebrew + Virtualenv 環境でMeCabのインストール : さりんじゃーのプログラミング日記](http://salinger.github.io/blog/2013/01/17/1/)

2. Install python packages

    ```
    $ cd SearchEngine
    $ pip install -r requirements.txt
    ```

3. Run

    ```
    $ python run.py
    ```


