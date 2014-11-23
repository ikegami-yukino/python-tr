python-tr
=========
.. image:: https://badge.fury.io/py/python-tr.svg
    :target: http://badge.fury.io/py/python-tr
.. image:: https://travis-ci.org/ikegami-yukino/python-tr.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/python-tr
.. image:: https://coveralls.io/repos/ikegami-yukino/python-tr/badge.png
    :target: https://coveralls.io/r/ikegami-yukino/python-tr


This module is a Python implementation of the tr algorithm.

tr(string1, string2, source, option='')

If not given option, then replace all characters in string1 with
the character in the same position in string2.

Following options are available:


c
    Replace all complemented characters in string1 with the character in the same position in string2.
d
    Delete all characters in string1.
s
    Squeeze all characters in string1.
cs
    Squeeze all the characters in string2 besides "c" replacement.
ds
    Delete all characters in string1. Squeeze all characters in string2.
cd
    Delete all complemented characters in string1.


Params:
 - <unicode> string1
 - <unicode> string2
 - <unicode> source
 - <basestring> option
Return:
 - <unicode> translated_source


Note
===========
- If Python2.x, the type of paramaters (string1, string2 and source) must be unicode.
- If Python3.3 or later, the type of paramaters (string1, string2 and source) must be str.


Example
===========
Python2.x

>>> from tr import tr
>>> tr(u'bn', u'cr', u'bunny')
u'curry'
>>> tr(u'n', '', u'bunny', 'd')
u'buy'
>>> tr(u'n', u'u', u'bunny', 'c')
u'uunnu'
>>> tr(u'n', u'', u'bunny', 's')
u'buny'
>>> tr(u'bn', '', u'bunny', 'cd')
u'bnn'
>>> tr(u'bn', u'cr', u'bunny', 'cs')
u'brnnr'
>>> tr(u'bn', u'cr', u'bunny', 'ds')
u'uy'


Python3.3 or later


>>> from tr import tr
>>> tr('bn', 'cr', 'bunny')
'curry'
>>> tr('n', '', 'bunny', 'd')
'buy'
>>> tr('n', 'u', 'bunny', 'c')
'uunnu'
>>> tr('n', '', 'bunny', 's')
'buny'
>>> tr('bn', '', 'bunny', 'cd')
'bnn'
>>> tr('bn', 'cr', 'bunny', 'cs')
'brnnr'
>>> tr('bn', 'cr', 'bunny', 'ds')
'uy'


Contributions are welcome.
