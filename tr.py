r"""UNIX-like transliteration

This module provides some operations for replacing or removing
specific characters from source.
"""

import re
import sys


if sys.version_info < (3, ):  # for Python 2.x
    valid_source_type = unicode
    chr = unichr
else:
    valid_source_type = str


def tr(string1, string2, source, option=''):
    """Replace or remove specific characters.

    If not given option, then replace all characters in string1 with
    the character in the same position in string2.

    Following options are available:
        c   Replace all complemented characters in string1 with
            the character in the same position in string2.
        d   Delete all characters in string1.
        s   Squeeze all characters in string1.
        cs  Squeeze all the characters in string2 besides "c" replacement.
        ds  Delete all characters in string1. Squeeze all characters
            in string2.
        cd  Delete all complemented characters in string1.

    Params:
        <unicode> string1
        <unicode> string2
        <unicode> source
        <basestring> option
    Return:
        <unicode> translated_source
    """

    def is_valid_type(source):
        return isinstance(source, valid_source_type)

    def make_char_list(source):
        char_list = []
        back_slash = False
        hyphen = False
        for char in source:
            if char == '\\':
                if not back_slash:
                    back_slash = True
                    continue
            elif char == '-' and not back_slash:
                hyphen = True
                continue
            elif hyphen:
                start = char_list[-1] + 1
                char_list += range(start, ord(char))
            char_list.append(ord(char))
            back_slash = False
            hyphen = False
        return char_list

    def to_unichr(char_list):
        return map(chr, char_list)

    def squeeze(from_list, source):
        for char in from_list:
            squeeze_pattern = re.compile('%s{2,}' % char)
            source = squeeze_pattern.sub(char, source)
        return source

    def translate(from_list, to_list, source):
        translate_dict = dict(zip(from_list, to_list))
        return source.translate(translate_dict)

    if not is_valid_type(source):
        raise TypeError('source string must be unicode')

    if option == 's':
        from_list = make_char_list(string1)
        from_list = to_unichr(from_list)
        return squeeze(from_list, source)
    elif 'c' in option:
        from_list = make_char_list(string1)
        from_list = to_unichr(from_list)
        from_list = [ord(c) for c in set(source) - set(from_list)]
        if 'd' in option:
            to_list = [None for i in from_list]
        else:
            to_list = [string2[-1] for i in from_list]
        source = translate(from_list, to_list, source)
        if 's' in option:
            source = squeeze(to_list, source)
        return source
    elif 'd' in option:
        from_list = make_char_list(string1)
        to_list = [None for i in from_list]
        source = translate(from_list, to_list, source)
        if 's' in option:
            to_list = make_char_list(string2)
            to_list = to_unichr(to_list)
            source = squeeze(to_list, source)
        return source
    else:
        from_list = make_char_list(string1)
        to_list = make_char_list(string2)
        to_list = to_unichr(to_list)
        return translate(from_list, to_list, source)
