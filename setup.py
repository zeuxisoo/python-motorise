#!/usr/bin/env python
# -*- coding: utf-8 -*-

import motorise
from email.utils import parseaddr
from setuptools import setup, find_packages

author, author_email = parseaddr(motorise.__author__)

setup(
    name='motorise',
    version=motorise.__version__,
    url='https://github.com/zeuxisoo/python-motorise/',
    license='BSD',
    author=author,
    author_email=author_email,
    description='A toy for automating interaction with websites',
    packages=find_packages('motorise'),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pytidylib'
    ]
)
