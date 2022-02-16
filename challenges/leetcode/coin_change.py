"""
Solution for LC#322: Coin Change

https://leetcode.com/problems/coin-change/
"""
import sys
from typing import List

INF = sys.maxsize

# dp approach with tabulation (bottom-up)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        # tabulation
        for k in range(amount + 1):
            for coin in coins:
                if k - coin >= 0:
                    dp[k] = min(dp[k], dp[k - coin] + 1)

        # if dp state == INF it means such amount was never reached so we return -1
        return dp[amount] if dp[amount] != INF else -1


# dp approach with memoization (top-down)
class SolutionMemoized:
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

        # if dp state == INF it means such amount was never reached so we return -1
        return c if c != INF else -1
