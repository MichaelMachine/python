#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---
# @Author: Michael
# @Software: Pycharm
# @file: db.py
# @Time: 2021/3/24 10:46 下午
# ---

"""
    g 是一个特殊对象，独立于每一个请求，在处理请求过程中，它可以用于存储可能多个函数都会用到的数据，把连接储存于其中，可以多次使用，而不用在
同一个请求中每次调用 get_db 时都创建一个新的连接；
    current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用，这里使用了应用工厂，那么在其余的代码中就不会出现应用对象，当应用创建后，
在处理一个请求时，get_db 会被调用，这样就需要使用 current_app；
    sqlite3.connect() 建立一个数据库连接，该连接指向配置中的 DATABASE 指定的文件，这个文件现在还没有建立，后面会在初始化数据库的时候建立
该文件。
    sqlite3.Row 告诉连接返回类似于字典的行，这样可以通过列名称来操作数据。
    close_db 通过检查 g.db 来确定连接是否已经建立。如果连接已经建立，那么就关闭连接。以后会在应用工厂中告诉应用 close_db 函数，这样每次
请求就会调用它。
"""
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database')


def init_app(app):
    app.teardown_appcontext(close_db)  # 告诉 Flask 在返回响应后进行清理的时候调用此函数
    app.cli.add_command(init_db_command)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
