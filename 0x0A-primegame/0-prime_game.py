#!/usr/bin/python3

"""
This module implements a game where Maria and Ben take turns
choosing prime numbers from a set of consecutive integers.
The player that cannot make a move loses the game.
The module provides a function to determine the
winner of each game.


"""


def isWinner(x, nums):
    """
    Determines the winner of each game based on the given number of
    rounds and sets of consecutive integers.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the sets of
        consecutive integers.

    Returns:
        str: The name of the player that won the most rounds.
        If the winner cannot be determined, returns None.

    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        numbers = set(range(1, n + 1))
        player = "Maria"

        while True:
            prime = None
            for num in numbers:
                if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                    prime = num
                    break

            if prime is None:
                break

            for num in range(prime, n + 1, prime):
                numbers.discard(num)

            if player == "Maria":
                player = "Ben"
            else:
                player = "Maria"

        if player == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
