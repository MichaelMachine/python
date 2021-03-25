#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---
# @Author: Michael
# @Software: Pycharm
# @file: test_factory.py
# @Time: 2021/3/25 11:25 下午
# ---
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'