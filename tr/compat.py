# -*- coding: utf-8 -*-
import sys


if sys.version_info < (3, ):  # for Python 2.x
    from itertools import imap, izip
    map = imap
    chr = unichr
    range = xrange
    zip = izip
    valid_source_type = unicode
else:
    map = map
    chr = chr
    range = range
    zip = zip
    valid_source_type = str
