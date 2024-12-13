#!/usr/bin/python3
"""
Module: Prime Game Winner

This module determines the winner of a game
played between Maria and Ben. The game involves
choosing prime numbers and removing them along
with their multiples from a set of consecutive integers.

Functions:
    isWinner(x, nums): Determines the overall
    winner after x rounds of the game.
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(max_n):
        """
        Generate a list of primes up to max_n
        using the Sieve of Eratosthenes.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    def count_prime_moves(n, is_prime):
        """Count the number of moves in the game given n."""
        numbers = list(range(1, n + 1))
        moves = 0
        for i in range(2, n + 1):
            if is_prime[i] and numbers[i - 1] != 0:
                moves += 1
                for j in range(i, n + 1, i):
                    numbers[j - 1] = 0
        return moves

    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_prime_moves(n, is_prime)
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
