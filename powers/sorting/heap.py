"""
Module with heapsort which runs in O(NlogN).
"""
import heapq
from typing import List

from powers.heap import MaxHeap
from powers.heap import MinHeap


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


def heapsort_with_minheap(arr: List) -> List:
    n = len(arr)
    min_heap = MinHeap(arr)

    # pops min values which automatically keeps heap invariant and returns values in asc order
    return [min_heap.pop_min() for _ in range(n)]


def heapsort_builtin(arr: List[int]) -> List:
    n = len(arr)
    heapq.heapify(arr)  # heapifies the list

    # pops min values
    return [heapq.heappop(arr) for _ in range(n)]
