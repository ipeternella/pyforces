"""
Module with selection sort which runs in O(N^2).
"""
from typing import List


def swap(arr: List, i: int, j: int) -> None:
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def selectionsort(arr: List) -> List:
    n = len(arr)
    for i in range(n):
        min_j = i

        # finds min in [i + 1, n)
        for j in range(i + 1, n):
            if arr[j] < arr[min_j]:
                min_j = j

        if min_j != i:
            swap(arr, i, min_j)

    return arr
