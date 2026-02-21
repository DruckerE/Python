"""Absolute Value."""


def abs_val(num: float) -> float:
    """
    Find the absolute value of a number.

    >>> abs_val(-5.1)
    5.1
    >>> abs_val(-5) == abs_val(5)
    True
    >>> abs_val(0)
    0
    """
    return -num if num < 0 else num


def abs_min(x: list[int]) -> int:
    """
    Find the element with the smallest absolute value.

    >>> abs_min([0, 5, 1, 11])
    0
    >>> abs_min([3, -10, -2])
    -2
    >>> abs_min([])
    Traceback (most recent call last):
        ...
    ValueError: abs_min() arg is an empty sequence
    """
    if not x:
        raise ValueError
