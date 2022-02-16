"""
Solution for LC#322: Coin Change

https://leetcode.com/problems/coin-change/
"""
import sys
from typing import List

INF = sys.maxsize

# dp approach with memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def change(target, dp):
            if target == 0:
                return 0

            if target < 0:
                return INF

            if dp[target] != -1:
                return dp[target]

            min_coins = INF
            for coin in coins:
                c = change(target - coin, dp)
                if c != INF:
                    min_coins = min(min_coins, c + 1)

            dp[target] = min_coins
            return dp[target]

        dp = [-1] * (amount + 1)
        c = change(amount, dp)
        return c if c != INF else -1
