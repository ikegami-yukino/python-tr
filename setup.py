# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='python-tr',
    py_modules=['tr'],
    version='0.0.1',
    license='MIT License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description='A Python implementation of the tr algorithm',
    author='Yukino Ikegami',
    author_email='yukino0131@me.com',
    url='https://github.com/ikegami-yukino/python-tr',
    keywords=['tr', 'transliterate', 'translate'],
    classifiers=[
        'Development Status :: 3 - Alpha',
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
        'Topic :: Text Processing'
        ],
    long_description=open('README.rst').read() + '\n\n' + open('CHANGES.rst').read()
)
