#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='sqldoc-impylaparser',
    version='0.1.0',
    author='Ivan Korhner',
    author_email='korhner@gmail.com',
    maintainer='Ivan Korhner',
    maintainer_email='korhner@gmail.com',
    license='MIT',
    url='https://github.com/korhner/sqldoc-impylaparser',
    description='Parse impala databases.',
    long_description=read('README.rst'),
    py_modules=['sqldoc_impylaparser'],
    install_requires=['sqldoc>=0.1.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: sqldoc',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'sqldoc_component': [
            'impylaparser = sqldoc_impylaparser:get_component',
        ],
    },
)
