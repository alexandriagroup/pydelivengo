#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

import setuptools

tests_require = [
    'pytest',
    'pytest-pep8',
    'pytest-cov',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydelivengo",
    version="1.6",
    license='MIT',
    author="Alicia FLOREZ",
    author_email="alicflorez@gmail.com",
    description="A lib to use MyDelivengo API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexandriagroup/pydelivengo",
    project_urls = {
        'Source': 'https://github.com/alexandriagroup/pydelivengo/archive/v1.5.tar.gz',
        'Documentation': 'https://alexandriagroup.github.io/pydelivengo/',
        'Travis': 'https://travis-ci.org/alexandriagroup/pydelivengo',
    },
    packages=['pydelivengo'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 5 - Production/Stable',
    ],
    keywords='api mydelivengo python3 webservices',

)
