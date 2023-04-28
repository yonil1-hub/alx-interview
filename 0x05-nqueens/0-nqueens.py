#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.

TODO:
    * Write a program that solves the N queens problem.
"""


def solve_n_queens(chess_board, row, queens_placed, solutions):
    """
    Args:
        chess_board (list)
        row (int)
        queens_placed (int)
        solutions (list)

    Returns:
        solutions (list)
    """
    if queens_placed == len(chess_board):
        solutions.append(get_solution(chess_board))
        return solutions

    for col in range(len(chess_board)):
        if chess_board[row][col] == -1:
            new_board = copy_board(chess_board)
            new_board[row][col] = 1
            cancel_vulnerable_positions(new_board, row, col)
            solutions = solve_n_queens(new_board, row + 1, queens_placed + 1, solutions)
    return solutions


def cancel_vulnerable_positions(chess_board, row, col):
    """
    Cancels out vulnerable positions for the queen

    Args:
        chess_board (list)
        row (int)
        col (int)
    """
    n = len(chess_board)
    """Cancel forward positions"""
    for c in range(col + 1, n):
        chess_board[row][c] = 0
    """Cancel backwards positions"""
    for c in range(col - 1, -1, -1):
        chess_board[row][c] = 0
    """Cancel down positions"""
    for r in range(row + 1, n):
        chess_board[r][col] = 0
    """Cancel up positions"""
    for r in range(row - 1, -1, -1):
        chess_board[r][col] = 0
    """Cancel right downward diagonal positions"""
    c = col + 1
    for r in range(row + 1, n):
        if c >= n:
            break
        chess_board[r][c] = 0
        c += 1
    """Cancel left upward diagonal positions"""
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chess_board[r][c] = 0
        c -= 1
    """Cancel right upward diagonal positions"""
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= n:
            break
        chess_board[r][c] = 0
        c += 1
    """Cancel left downward diagonal positions"""
    c = col - 1
    for r in range(row + 1, n):
        if c < 0:
            break
        chess_board[r][c] = 0
        c -= 1


def create_chess_board(n):
    """
    Create a board of size N * N
    """
    chess_board = []

    """Create rows"""
    for row in range(n):
        chess_board.append([])

    """Create columns"""
    for row in chess_board:
        for col in range(n):
            row.append(-1)

    return chess_board


def copy_board(chess_board):
    """
    make a copy of chess_board
    """
    if isinstance(chess_board, list):
        """Recursively copy"""
        return list(map(copy_board, chess_board))
    return chess_board


def get_solution(chess_board):
    """
    Extract the required outcome
    """
    outcome = []
    for row in range(len(chessBoard)):
        for col in range(len(chessBoard)):
            if chessBoard[row][col] == 1:
                outcome.append([row, col])
                break
    return (outcome)


def execute():
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isnumeric() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess = chessBoard(int(sys.argv[1]))
    resultMatrix = queens(chess, 0, 0, [])
    for row in resultMatrix:
        print(row)


if __name__ == '__main__':
    execute()
