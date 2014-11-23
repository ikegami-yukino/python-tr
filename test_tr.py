# -*- coding: utf-8 -*-
from nose.tools import assert_equals, assert_raises
from tr import tr
import sys


def test_no_option():
    assert_equals(tr('ab', 'cd', u'ab'), 'cd')
    assert_equals(tr('a-z', 'A-Z', u'ab'), 'AB')
    assert_equals(tr('a\-b', 'cde', u'a-b'), 'cde')


def test_complement():
    assert_equals(tr(u'ab', u'\-', u'123', 'c'), u'---')


def test_delete():
    assert_equals(tr('ab', '', u'abc', 'd'), 'c')
    assert_equals(tr('\\', '', u'\\a\\', 'd'), 'a')


def test_squeeze():
    assert_equals(tr('a', '', u'aabcaa', 's'), 'abca')


def test_cd():
    assert_equals(tr('ab', '', u'abc', 'cd'), 'ab')
    assert_equals(tr('ab', '', u'abcabcabc', 'cd'), 'ababab')


def test_cs():
    assert_equals(tr('a', u'0', u'aa11', 'cs'), 'aa0')
    assert_equals(tr('a', u'0', u'11aa11', 'cs'), '0aa0')


def test_ds():
    assert_equals(tr('a', u'0', u'aa00', 'ds'), '0')
    assert_equals(tr('a-z', u'0-9', u'aa00', 'ds'), '0')


def test_invalid_value():
    if sys.version_info >= (3,):
        source = 'あ'.encode('utf8')
    else:
        source = 'あ'
    assert_raises(TypeError, tr, *['a', 'b', source, 'd'])
