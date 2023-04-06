#!/usr/bin/env python3

"""Minimum Operations"""


def minOperations(n: int) -> int:
    """
    Returns the fewest number of operations needed to result in exactly n H
    characters in a text file that initially contains a single H character,
    using only the operations of Copy All and Paste.
    If n is impossible to achieve, returns 0.
    """
    if not isinstance(n, int) or n < 1:
        return 0

    operations = 0
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            n //= i
            operations += i
        if n == 1:
            break
    if n > 1:
        operations += n
    return operations
