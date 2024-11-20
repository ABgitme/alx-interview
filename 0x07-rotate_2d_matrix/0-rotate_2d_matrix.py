#!/usr/bin/python3
"""rotate an matrix 90 degrees clockwise in-place"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list of list of int): The matrix to be rotated.
    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):  # Start from i to avoid redundant swaps
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
