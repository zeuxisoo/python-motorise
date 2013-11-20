#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.utils import parseaddr
from setuptools import setup, find_packages

__version__ = '0.1.0'
__author__ = 'Zeuxis Lo <seekstudio@gmail.com>'

author, author_email = parseaddr(__author__)

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='motorise',
    version=__version__,
    url='https://github.com/zeuxisoo/python-motorise/',
    license='BSD',
    author=author,
    author_email=author_email,
    description='A toy for automating interaction with websites',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requires,
)
