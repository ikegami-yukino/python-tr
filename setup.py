# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup

with open(os.path.join('tr', '__init__.py'), 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='python-tr',
    packages=['tr'],
    version=version,
    license='MIT License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description='A Pure-Python implementation of the tr algorithm',
    author='Yukino Ikegami',
    author_email='yukino0131@me.com',
    url='https://github.com/ikegami-yukino/python-tr',
    keywords=['tr', 'transliterate', 'translate'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: General'
        ],
    long_description=open('README.rst').read() + '\n\n' + open('CHANGES.rst').read()
)
