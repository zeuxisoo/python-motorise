#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.utils import parseaddr
from setuptools import setup, find_packages

__version__ = '0.1.7'
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
    description='A toy for automating interaction with websites like mechanize',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Browsers"
    ],
)
