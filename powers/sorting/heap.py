"""
Module with heapsort which runs in O(NlogN).
"""
import heapq
from typing import List

from powers.heap import MaxHeap
from powers.heap import MinHeap


def heapify(arr: List, parent_i: int, size: int):
    left_i = 2 * parent_i + 1
    right_i = 2 * parent_i + 2
    biggest_i = parent_i

    if left_i < size and arr[left_i] > arr[biggest_i]:
        biggest_i = left_i

    if right_i < size and arr[right_i] > arr[biggest_i]:
        biggest_i = right_i

    if biggest_i != parent_i:
        arr[parent_i], arr[biggest_i] = arr[biggest_i], arr[parent_i]  # swap
        heapify(arr, biggest_i, size)


def heapsort(arr):
    n = len(arr)

    # builds max heap in the array
    for i in range(n // 2 - 1, -1, -1):  # [n // 2 .. 0]
        heapify(arr, i, n)

    for i in range(n - 1, 0, -1):  # [n - 1 .. 1]
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


def heapsort_with_maxheap(arr: List) -> List:
    """
    Heapsort using custom MaxHeap data structure.
    """
    n = len(arr)
    max_heap = MaxHeap(arr)

    for i in range(n - 1, 0, -1):  # [n - 1 .. 1]
        arr[0], arr[i] = arr[i], arr[0]  # max (arr[0]) is swapped to the end
        max_heap.heapify(0, i)  # keep the heap! i reduces the size of the heap!

    return arr


def heapsort_with_minheap(arr: List) -> List:
    """
    Heapsort using custom MinHeap data structure.
    """
    n = len(arr)
    min_heap = MinHeap(arr)

    # pops min values which automatically keeps heap invariant and returns values in asc order
    return [min_heap.pop_min() for _ in range(n)]


def heapsort_builtin(arr: List[int]) -> List:
    """
    Heapsort using built-in min heap from heapq module.
    """
    n = len(arr)
    heapq.heapify(arr)  # heapifies the list

    # pops min values
    return [heapq.heappop(arr) for _ in range(n)]
