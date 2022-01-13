"""
Solution for LC#347: Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/
"""
from collections import Counter
from typing import Dict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freq_lists: Dict[int, List[int]] = dict()
        k_most_freq = []

        for num, freq in freqs.items():
            if freq in freq_lists:
                freq_lists[freq].append(num)
            else:
                freq_lists[freq] = [num]

        # traverse highest frequencies first to get k-most freq nums from freq_lists
        # freq_lists.keys() contains only unique freqs
        for f in sorted(freq_lists.keys(), reverse=True):
            freq_list = freq_lists[f]
            i = 0

            while i < len(freq_list):
                k_most_freq.append(freq_list[i])
                i += 1

                if len(k_most_freq) == k:
                    return k_most_freq

        return []
