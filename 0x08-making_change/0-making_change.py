#!/usr/bin/python3

def makeChange(coins, total):
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
