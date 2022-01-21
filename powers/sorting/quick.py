"""
Module with quicksort implementation which is also based on Divide And Conquer
algorithmic paradigm.
"""

from typing import List


def partition(arr: List, l: int, r: int) -> int:
    """
    Partitions an array into two subarrays around the returned index q in which:
        - arr[i] <= arr[q] <= arr[j] for i <= q <= j

    Example:
        [6,0,2,7,5] returns q = 2 and [0,2,_5_,6,7] (pivot at the correct index q == 2)
    """
    pivot = arr[r]  # pick last element
    i = l - 1  # i starts off the subarray

    for j in range(l, r):  # do not include the pivot: [l .. r - 1], so no a[r]!
        if arr[j] <= pivot:
            i += 1  # increment the last swapped ix
            arr[i], arr[j] = arr[j], arr[i]

    i += 1  # final partition index: pivot's position
    arr[i], arr[r] = arr[r], arr[i]
    return i  # return the final partition's index


def quicksort(arr: List) -> None:
    def quicksort_aux(arr: List, l: int, r: int) -> None:
        if l < r:
            q = partition(arr, l, r)  # q is the partition point
            quicksort_aux(arr, l, q - 1)
            quicksort_aux(arr, q + 1, r)

    quicksort_aux(arr, 0, len(arr) - 1)
