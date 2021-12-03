"""
Solution for: Minimum Swaps 2

https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""
import heapq
from typing import Dict
from typing import List


def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    indices: Dict[int, int] = dict()
    mins: List[int] = arr.copy()

    heapq.heapify(mins)  # asymptotically tight is O(N), not O(NLogN) - CLRS for details.
    for i in range(n):  # O(N)
        indices[arr[i]] = i

    # adapted selection sort (provides min swaps) with a heap to provide quicker access to mins without O(N) scans!
    # O(NlogN) ~ should be sufficient for n = 10^5
    for i in range(n):
        next_min = heapq.heappop(mins)  # for N runs: O(NlogN)

        if arr[i] > next_min:
            swaps += 1
            min_i = indices[next_min]

            # update indices and then swap!
            indices[arr[i]], indices[next_min] = indices[next_min], indices[arr[i]]
            arr[i], arr[min_i] = arr[min_i], arr[i]

    return swaps
