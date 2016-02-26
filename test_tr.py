# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nose.tools import assert_equals, assert_raises
from tr import tr


def test_no_option():
    assert_equals(tr('ab', 'cd', 'ab'), 'cd')
    assert_equals(tr('a-z', 'A-Z', 'ab'), 'AB')
    assert_equals(tr('a\-b', 'cde', 'a-b'), 'cde')
    assert_equals(tr('1-9', 'A-I', '8429503671'), 'HDBIE0CFGA') #=> OK
    assert_equals(tr('1-9', 'ABC#', '8429503671'), '##B##0C##A') #=> '8#B950C67A'
    assert_equals(tr('^1-9', '@', '8429503671'), '84295@3671') #=> '8429503671'


def test_complement():
    assert_equals(tr('ab', '\-', '123', 'c'), '---')


def test_delete():
    assert_equals(tr('ab', '', 'abc', 'd'), 'c')
    assert_equals(tr('\\', '', '\\a\\', 'd'), 'a')


def test_squeeze():
    assert_equals(tr('a', '', 'aabcaa', 's'), 'abca')
    assert_equals(tr('$', '', '$$$$a', 's'), '$a')


def test_cd():
    assert_equals(tr('ab', '', 'abc', 'cd'), 'ab')
    assert_equals(tr('ab', '', 'abcabcabc', 'cd'), 'ababab')


def test_cs():
    assert_equals(tr('a', '0', 'aa11', 'cs'), 'aa0')
    assert_equals(tr('a', '0', '11aa11', 'cs'), '0aa0')


def test_ds():
    assert_equals(tr('a', '0', 'aa00', 'ds'), '0')
    assert_equals(tr('a-z', '0-9', 'aa00', 'ds'), '0')


def test_invalid_value():
    source = 'あ'.encode('utf8')
    assert_raises(TypeError, tr, *['a', 'b', source, 'd'])
