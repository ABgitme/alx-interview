#!/usr/bin/python3
"""
Module for generating Pascal's triangle.

This module contains a function that returns a list of lists representing
Pascal's triangle for a given number of rows. Each row in the triangle
contains integers that represent the coefficients of the binomial expansion.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle with n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.
        Must be a non-negative integer.

    Returns:
        list: A list of lists containing
        integers that represent Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        # Start each new row with a 1 and build the middle values
        row = [1] + [
            triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i)
            ] + [1]
        triangle.append(row)  # Append the constructed row to the triangle

    return triangle
