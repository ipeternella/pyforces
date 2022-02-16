"""
Solution for LC#518: Coin Change 2

https://leetcode.com/problems/coin-change-2/
"""
from typing import List


# DP tabulated approach: O(amount * len(coins))
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * n for _ in range(amount + 1)]  # dp[amount][max_coin_index] = ways

        for i in range(n):
            dp[0][i] = 1

        for target in range(1, amount + 1):
            max_so_far = 0
            for i in range(n):
                c = coins[i]

                if target - c >= 0:
                    dp[target][i] = dp[target - c][i] + max_so_far
                    max_so_far = max(max_so_far, dp[target][i])
                else:
                    dp[target][i] = max_so_far  # if coin value is too much: max_so_far takes place

        return dp[amount][n - 1]


class SolutionMemoized:
    def change(self, amount: int, coins: List[int]) -> int:
        def change(amount, start, dp):
            if amount < 0:
                return 0

            if amount == 0:
                return 1  # amount zero: zero coins is one way (base case)

            if dp[amount][start] != -1:
                return dp[amount][start]

            ways = 0
            for i in range(start, len(coins)):
                # useless going further: negative paths return 0 (only because we sorted coins!)
                if amount - coins[i] < 0:
                    break

                # amount - coins[i]: pick coins[i] and reduce it from the amount!
                ways += change(amount - coins[i], i, dp)

            dp[amount][start] = ways
            return dp[amount][start]

        n = len(coins)
        coins.sort()

        # to avoid duplicated ways while counting: use two variables in the state: change amount and index of coins
        dp = [[-1] * n for _ in range(amount + 1)]

        return change(amount, 0, dp)
