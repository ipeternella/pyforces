"""
Solution for LC#1011: Capacity To Ship Packages Within D Days

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def load_days(capacity):
            curr_days, curr_weight = 0, 0
            for weight in weights:
                curr_weight += weight

                if curr_weight > capacity:
                    curr_days += 1
                    curr_weight = weight

            curr_days += 1  # last day
            return curr_days

        min_c, max_c = max(weights), sum(weights)
        while min_c < max_c:  # shrink the search space until 1 element is left
            mid_c = (min_c + max_c) // 2
            d = load_days(mid_c)

            if d > days:  # we need more capacity: more days are required than the target
                min_c = mid_c + 1
            else:  # reduce the capacity: less days than needed
                max_c = mid_c

        return min_c
