"""
Solution for LC#347: Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/
"""
from collections import Counter
from typing import Dict
from typing import List


def init_heap(nums):
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, i)


def heapify(heap, i):
    n = len(heap)
    l, r = 2 * i + 1, 2 * i + 2
    biggest = i  # parent

    if l <= n - 1 and heap[l][0] > heap[i][0]:  # first element = freq
        biggest = l

    if r <= n - 1 and heap[r][0] > heap[biggest][0]:
        biggest = r

    if biggest != i:
        heap[biggest], heap[i] = heap[i], heap[biggest]
        heapify(heap, biggest)


def get_max(heap):
    n = len(heap)
    max_value = heap[0]

    heap[0] = heap[n - 1]
    heap.pop()
    heapify(heap, 0)

    return max_value


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_most = []

        # all O(N) operations
        freqs = Counter(nums)
        freq_heap = [(freq, num) for num, freq in freqs.items()]
        init_heap(freq_heap)  # asymptotically tight: O(N) too!

        while k > 0:
            _, num = get_max(freq_heap)
            k_most.append(num)
            k -= 1

        return k_most


class SolutionSorting:
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
