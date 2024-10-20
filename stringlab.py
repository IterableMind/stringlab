"""
This is a silly python module that implement str methods in pure
python.

N/B Python's original str methods are faster and are optimized and
should be considered first.
"""

def _is_ascii_upper(c):
    return 'A' <= c <= 'Z'

def _is_ascii_lower(c):
    return 'a' <= c <= 'z'


class Text(str):
    """
    Extend and overwrite common methods present
    in str class.
    """
    def upper(self):
        """Overwrite the original upper().
            This method only handles ASCII characters, not Unicode.
        """

        if all(_is_ascii_upper(c) for c in self):
            # all characters are already uppercase.
            return self

        uppercased_chars = []
        for c in self:
            if _is_ascii_lower(c):
                uppercased_chars.append(chr(ord(c) - 32))
            else:
                uppercased_chars.append(c)

        return ''.join(uppercased_chars)

    def lower(self):
        """Overwrite the original lower().
            This method only handles ASCII characters, not Unicode.
        """
        if all(_is_ascii_lower(c) for c in self):
            # all characters are already lowercase
            return self

        lowercased_chars = []
        for c in self:
            if _is_ascii_upper(c):
                lowercased_chars.append(chr(ord(c) + 32))
            else:
                lowercased_chars.append(c)
        return ''.join(lowercased_chars)

        

    def endswith(self, s, *args):
        # Overwrite the default str.endswith()

        start, end = 0, len(self)

        if len(args) > 2:
            raise TypeError('endswith() takes at most 3 '
                    f'argments (given {len(args) + 1})')

        if not isinstance(s, (str, tuple)):
            raise TypeError('endswith()1 first arg must be str '
                f'or a tuple of str, not \'{s.__class__.__name__}\'')
        if isinstance(s, tuple) and not \
            all((isinstance(item, str) for item in s)):
            raise TypeError(f'tuple for endswith must only contain str')

        if not all((isinstance(arg, int) for arg in args)):
            raise TypeError('slice indices must be integers')

        if len(args) == 1:
            start = args[0]
        elif len(args) == 2:
            start, end = args

        if s == '':
            return True # all strings ends with ''

        if isinstance(s, tuple):
            return any(self[start:end].endswith(sub) for sub in s)
        else:
            substrlen = -len(s)
            if not start and end == len(self):
                return s == self[substrlen:]
            newsubstr = self[start:end]
            return s == newsubstr[substrlen:]



if __name__ == '__main__':
    # simple tests
    print('Running tests...')
    s = Text('Hello world again')
    assert s.endswith('again') == True
    assert s.endswith('ld', 0, 11) == True
    assert s.endswith(('world', 'python')) == False
    assert s.endswith(('world', 'in', 'python')) == True
    assert s.endswith(('world', 'in', 'lo'), 1, 5) == True
    assert Text('@jared').upper() == '@JARED'
    assert Text('#oYaRo').lower() == '#oyaro'
