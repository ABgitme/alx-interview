#!/usr/bin/python3
"""This module defines a function minOperations that calculates
the fewest number of operations needed to result in exactly
n 'H' characters in a text file, starting from one 'H'."""


def minOperations(n):
    """Calculate the fewest number of
    operations to result in exactly n 'H' characters"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factorize n by dividing it by the smallest possible divisor at each step
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
