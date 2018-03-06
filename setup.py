#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

from setuptools import setup

tests_require = [
    'pytest',
    'pytest-pep8',
    'pytest-cov',
]

setup(
    name='pydelivengo',
    license='MIT',
    version = 'v1.2',
    description = 'A lib to use MyDelivengo API',
    author = 'Alicia FLOREZ',
    author_email = 'alicflorez@gmail.com',
    url = 'https://github.com/alexandriagroup/pydelivengo',
    download_url = 'https://github.com/alexandriagroup/pydelivengo/archive/v1.2.tar.gz',
    keywords=['api', 'mydelivengo', 'python', 'webservices'],
    packages=['pydelivengo'],
)
