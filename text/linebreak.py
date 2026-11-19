"""文本断行：贪心、两端对齐与断字：待实现的核心模块。"""


def measure(text, widths):
    """按字宽测量文本。"""
    raise NotImplementedError

def greedy_break(words, widths, max_width):
    """贪心断行。"""
    raise NotImplementedError

def justify(words, width, widths):
    """两端对齐。"""
    raise NotImplementedError

def hyphenate(word, limit):
    """按上限断字。"""
    raise NotImplementedError

def count_lines(words, widths, max_width):
    """统计行数。"""
    raise NotImplementedError
