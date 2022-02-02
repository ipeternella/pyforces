"""
Solution for LC#121: Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import sys
from typing import List

INF = sys.maxsize


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = INF
        max_profit = 0
        for i in range(n):
            # always look for a min_price for each price[i] to maximize the selling difference
            # all the price diffs related to min_price are guaranteed to be the in the future
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit
