#!/usr/bin/python3

"""
This module implements a game where Maria and Ben take turns choosing prime
numbers from a set of consecutive integers. The player that cannot make a
move loses the game. Themodule provides a function to
determine the winner of each game.
"""


def isWinner(x, nums):
    """
    Determines the winner of each game based on the given number of rounds
    Args:
        x (int): The number of rounds.
        nums (list): An array of integers

    Returns:
        str: The name of the player that won the most rounds.
        If the winner cannot be
        determined, returns None.

    """

    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.

        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(is_prime(i) for i in range(1, n + 1))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
