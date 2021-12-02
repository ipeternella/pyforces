"""
Module with insertion sort which runs in O(N^2).
"""
from typing import List


def insertionsort(arr: List) -> List:
    n = len(arr)

    for i in range(1, n):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            # shifts right all elements smaller than key until key position is found
            arr[j + 1] = arr[j]
            j -= 1

        # inserts key at its proper position, so arr[0 .. j] is sorted
        arr[j + 1] = key

    return arr
