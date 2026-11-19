import pytest

from text import linebreak as mod

CASES = [
    ('measure', ['abc', {'a': 2, 'b': 1, 'c': 1}], 4, False),
    ('greedy_break', [['aa', 'bb', 'cc'], {'a': 1, 'b': 1, 'c': 1}, 5], ['aa bb', 'cc'], False),
    ('greedy_break', [['aaa', 'bb'], {'a': 1, 'b': 1}, 4], ['aaa', 'bb'], False),
    ('justify', [['a', 'b'], 5, {}], 'a   b', False),
    ('justify', [['a'], 5, {}], 'a', False),
    ('hyphenate', ['abcdefg', 3], ['abc', 'def', 'g'], False),
    ('count_lines', [['aa', 'bb', 'cc'], {}, 5], 2, False),
    ('measure', ['', {}], 0, False),
    ('measure', ['', {'a': 2}], 0, False),
    ('greedy_break', [['a', 'b', 'c'], {}, 3], ['a b', 'c'], False),
    ('justify', [['aa', 'bb'], 8, {}], 'aa    bb', False),
    ('hyphenate', ['ab', 5], ['ab'], False),
    ('hyphenate', ['', 2], [], False),
    ('count_lines', [['a', 'b'], {}, 1], 2, False),
    ('count_lines', [[], {}, 5], 0, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_linebreak_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
