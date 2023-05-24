#!/usr/bin/python3
"""
    file: 0-island_perimeter.py
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.
    Args:
        grid (List[List[int]]): A list of list of integers
        representing the island.
    Returns:
        The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
