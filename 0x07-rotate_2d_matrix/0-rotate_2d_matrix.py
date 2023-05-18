#!/usr/bin/python3
"""
    Rotate the matrix
"""


def rotate_2d_matrix(matrix):
    """
        This function rotate the 2D matrix.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]