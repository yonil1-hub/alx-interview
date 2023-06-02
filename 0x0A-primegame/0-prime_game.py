#!/usr/bin/python3

"""
This module implements a game where Maria and Ben take turns choosing prime
numbers from a set of consecutive integers. The player that cannot make a
move loses the game. Themodule provides a function to
determine the winner of each game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the game.
    Args:
        x (int): the number of rounds in the game.
        nums (list): a list of n integers representing the set of numbers
        from which the player can choose.
    Returns:
        The name of the player that won the most rounds. If the winner cannot
        be determined, return None.
    """
    if x <= 0 or nums is None or len(nums) == 0:
        return None
    n = max(nums)
    primes = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    player = 0
    for i in range(x):
        player += primes[nums[i]]
    if player * 2 == primes[nums[-1]]:
        return None
    if player * 2 > primes[nums[-1]]:
        return "Maria"
    return "Ben"
