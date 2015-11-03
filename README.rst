python-tr
==========

|travis| |coveralls| |downloads| |version| |license|


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

Installation
==============

::

  pip install python-tr


Example
===========
Python2.x

.. code:: python

    from tr import tr
    tr(u'bn', u'cr', u'bunny')
    # => u'curry'
    tr(u'n', '', u'bunny', 'd')
    # => u'buy'
    tr(u'n', u'u', u'bunny', 'c')
    # => u'uunnu'
    tr(u'n', u'', u'bunny', 's')
    # => u'buny'
    tr(u'bn', '', u'bunny', 'cd')
    # => u'bnn'
    tr(u'bn', u'cr', u'bunny', 'cs')
    # => u'brnnr'
    tr(u'bn', u'cr', u'bunny', 'ds')
    # => u'uy'


Python3.3 or later

.. code:: python

    from tr import tr
    tr('bn', 'cr', 'bunny')
    # => 'curry'
    tr('n', '', 'bunny', 'd')
    # => 'buy'
    tr('n', 'u', 'bunny', 'c')
    # => 'uunnu'
    tr('n', '', 'bunny', 's')
    # => 'buny'
    tr('bn', '', 'bunny', 'cd')
    # => 'bnn'
    tr('bn', 'cr', 'bunny', 'cs')
    # => 'brnnr'
    tr('bn', 'cr', 'bunny', 'ds')
    # => 'uy'


Contributions are welcome.


.. |travis| image:: https://travis-ci.org/ikegami-yukino/python-tr.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/python-tr
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/python-tr/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/python-tr?branch=master
    :alt: coveralls.io

.. |downloads| image:: https://img.shields.io/pypi/dm/python-tr.svg
    :target: http://pypi.python.org/pypi/python-tr/
    :alt: downloads

.. |version| image:: https://img.shields.io/pypi/v/python-tr.svg
    :target: http://pypi.python.org/pypi/python-tr/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/python-tr.svg
    :target: http://pypi.python.org/pypi/python-tr/
    :alt: license

