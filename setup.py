#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists
from setuptools import setup, find_packages

author = 'Matthias Baer'
email = 'matthias.r.baer@googlemail.com'
description = 'Some tools for matplotlib'
name = 'mplshared'
year = '2022'
url = 'https://github.com/maroba/mplshared'
version = '0.1.0'

setup(
    name=name,
    author=author,
    author_email=email,
    url=url,
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license='MIT',
    description=description,
    long_description=open('README.rst').read() if exists('README.rst') else '',
    long_description_content_type="text/markdown",
    install_requires=['sphinx', 'matplotlib', 'numpy'
                      ],
    python_requires=">=3.6",
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 ],
    platforms=['ALL'],
)
