"""
Solution for LC#15: 3Sum

https://leetcode.com/problems/3sum/
"""
from typing import Dict
from typing import List
from typing import Set
from typing import Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> Set[Tuple[int, ...]]:
        n = len(nums)
        triplets = set()
        checked = set()
        freqs: Dict[int, int] = dict()

        for j in range(n):
            freqs[nums[j]] = freqs.get(nums[j], 0) + 1

        for i in range(n):
            if nums[i] in checked:
                continue

            target = -nums[i]
            freqs[nums[i]] -= 1
            for j in range(i + 1, n):
                b = nums[j]
                freqs[b] -= 1
                needed = target - b

                if freqs.get(needed, 0) > 0:
                    triplets.add(tuple(sorted([b, needed, nums[i]])))

                freqs[b] += 1

            freqs[nums[i]] += 1
            checked.add(nums[i])

        return triplets
