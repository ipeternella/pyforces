"""
Module with heapsort which runs in O(NlogN).
"""
from typing import List

from powers.heap import MaxHeap


def swap(arr: List, i: int, j: int) -> None:
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def heapsort(arr: List) -> List:
    n = len(arr)
    max_heap = MaxHeap(arr)

    for i in range(n - 1, 0, -1):  # [n - 1 .. 1]
        swap(arr, 0, i)  # max is swapped to the end
        max_heap.heapify(0, i)  # keep the heap! i reduces the size of the heap!

    return arr
