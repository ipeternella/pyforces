"""
Solution for LC#122: Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            # when the price decreases between two days, we can always opt not to sell and
            # make profit of zero. Hence, we just have to add the price diffs when they are
            # positive as buying and selling on consecutive days always yields the max profit
            max_profit += max(0, prices[i] - prices[i - 1])

        return max_profit
