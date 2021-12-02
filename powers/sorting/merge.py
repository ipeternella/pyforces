"""
Mergesort algorithm which runs in O(NlogN).
"""
import sys
from typing import List

INF = sys.maxsize


def merge_sorted_subarrays(arr: List, p: int, q: int, r: int) -> None:
    """
    Merges sorted subarrays: arr[p .. q] and arr[q + 1 .. r].
    """
    n_left = q - p + 1
    n_right = r - q
    left = [INF] * (n_left + 1)  # + 1 for sentinel
    right = [INF] * (n_right + 1)

    for i in range(n_left):
        left[i] = arr[p + i]  # arr[p .. q]

    for i in range(n_right):
        right[i] = arr[q + 1 + i]  # arr[q + 1 .. r]

    left_i = 0
    right_i = 0
    for k in range(p, r + 1):  # total of r - p + 1 elements to place in arr
        if left[left_i] < right[right_i]:
            arr[k] = left[left_i]
            left_i += 1
        else:
            arr[k] = right[right_i]
            right_i += 1


def mergesort(arr: List) -> List:
    def mergesort_slice(p: int, r: int) -> None:
        # base case: subarray of size 1 is already sorted
        if p >= r:
            return

        # slice the arr into two subarrays until base case! Then merge the sorted subarrays
        q = (p + r) // 2
        mergesort_slice(p, q)
        mergesort_slice(q + 1, r)
        merge_sorted_subarrays(arr, p, q, r)

    mergesort_slice(0, len(arr) - 1)
    return arr
