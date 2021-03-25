#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---
# @Author: Michael
# @Software: Pycharm
# @file: setup.py
# @Time: 2021/3/25 11:11 下午
# ---
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
