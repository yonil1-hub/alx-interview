#!/usr/bin/python3
"""A module for finding the minimum number of coins required to
make a given amount.

This module contains a function that takes in a list of coin denominations and
a total amount, and returns the minimum number of coins required to make the
total amount using the coins provided.
"""


def find_minimum_coins(coins, total):
    """Finds the minimum number of coins required to make the given total.

    Args:
        coins: A list of integers representing the denominations of the coins
        available.
        total: An integer representing the total amount to be made.

    Returns:
        An integer representing the minimum number of coins required to make
        the given total. If it's not possible to make the total using the
        provided coins, returns -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    counter = 0

    for coin in coins:
        if coin > total:
            continue
        counter += total // coin
        total %= coin
        if total == 0:
            return counter

    return -1
