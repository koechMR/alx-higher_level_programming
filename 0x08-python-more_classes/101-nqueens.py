#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    """Recursive function to solve the N-Queens problem"""
    if col == len(board):
        # Base case: All queens are placed, print the solution
        print([[i, j] for i in range(len(board))
               for j in range(len(board)) if board[i][j] == 1])
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur for the next column
            solve_n_queens(board, col + 1)

            # Backtrack and remove the queen from board[i][col]
            board[i][col] = 0


def nqueens(n):
    """Solves the N-Queens problem for a given board size N"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve_n_queens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
