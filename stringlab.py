"""
This is a silly python module that implement str methods in pure
python.

N/B Python's original str methods are faster and are optimized and
should be considered first.
"""

class Text(str):
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

        return False



if __name__ == '__main__':
    # simple tests
    s = Text('Hello world again')
    assert s.endswith('again') == True
    assert s.endswith('ld', 0, 11) == True
    assert s.endswith(('world', 'python')) == False
    assert s.endswith(('world', 'in', 'python')) == True
    assert s.endswith(('world', 'in', 'lo'), 1, 5) == True
