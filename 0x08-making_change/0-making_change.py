#!/usr/bin/python3
"""
Module: make_change
This module provides a function to determine the fewest
number of coins needed to make a given total using a list
of coin denominations. It uses a dynamic
programming approach to compute the solution efficiently.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to make
    a given total using a list of coin denominations.
    This function uses a dynamic programming approach
    to compute the solution efficiently.

    Parameters:
    coins (list[int]): A list of coin denominations.
    Each element in the list represents a valid coin denomination.
    total (int): The total amount for which the fewest
    number of coins is to be determined.

    Returns:
    int: The fewest number of coins needed to make
    the given total. If it is not possible to make the
    total using the given coins, return -1.
    """
    if total <= 0:
        return 0

    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make 0 total

    # Update DP array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return result
    return dp[total] if dp[total] != float('inf') else -1
