"""
Simple and short min and max heap implementations to use as Python's heapq module
only contains a min heap implementation.
"""
import math
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar

T = TypeVar("T")


class MaxHeap(Generic[T]):
    heap: List[T]

    def __init__(self):
        self.heap = []

    def __len__(self) -> int:
        return len(self.heap)

    def parent(self, i: int) -> int:
        return math.ceil(i / 2) - 1

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def increase_key(self, i: int, new_key: T) -> None:
        if new_key < self.heap[i]:  # type: ignore
            raise ValueError(f"Key {new_key} is less than {self.heap[i]}")

        self.heap[i] = new_key
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:  # type: ignore
            self._swap(i, self.parent(i))
            i = self.parent(i)  # dont store parent_it or when i changes, parent_it must be updated!

    def insert(self, key: T):
        self.heap.append(key)
        self.increase_key(len(self) - 1, key)

    def heapify(self, parent_i: int) -> None:
        left_i = self.left_child(parent_i)
        right_i = self.right_child(parent_i)
        biggest_i = parent_i
        size = len(self.heap)

        if left_i < size and self.heap[parent_i] < self.heap[left_i]:  # type: ignore
            biggest_i = left_i

        if right_i < size and self.heap[biggest_i] < self.heap[right_i]:  # type: ignore
            biggest_i = right_i

        if biggest_i != parent_i:
            self._swap(biggest_i, parent_i)
            self.heapify(biggest_i)

    def pop_max(self) -> Optional[T]:
        size = len(self)

        if size < 1:
            return None

        key = self.heap[0]
        self._swap(0, size - 1)
        self.heap.pop()
        self.heapify(0)

        return key

    def _swap(self, i: int, j: int) -> None:
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


class MinHeap(Generic[T]):
    heap: List[T]

    def __init__(self):
        self.heap = []

    def __len__(self) -> int:
        return len(self.heap)

    def parent(self, i: int) -> int:
        return math.ceil(i / 2) - 1

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def decrease_key(self, i: int, new_key: T) -> None:
        if new_key > self.heap[i]:  # type: ignore
            raise ValueError(f"Key {new_key} is bigger than {self.heap[i]}")

        self.heap[i] = new_key
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:  # type: ignore
            self._swap(i, self.parent(i))
            i = self.parent(i)  # dont store parent_it or when i changes, parent_it must be updated!

    def insert(self, key: T):
        self.heap.append(key)
        self.decrease_key(len(self) - 1, key)

    def heapify(self, parent_i: int) -> None:
        left_i = self.left_child(parent_i)
        right_i = self.right_child(parent_i)
        smallest_i = parent_i
        size = len(self.heap)

        if left_i < size and self.heap[parent_i] > self.heap[left_i]:  # type: ignore
            smallest_i = left_i

        if right_i < size and self.heap[smallest_i] > self.heap[right_i]:  # type: ignore
            smallest_i = right_i

        if smallest_i != parent_i:
            self._swap(smallest_i, parent_i)
            self.heapify(smallest_i)

    def pop_min(self) -> Optional[T]:
        size = len(self)

        if size < 1:
            return None

        key = self.heap[0]
        self._swap(0, size - 1)
        self.heap.pop()
        self.heapify(0)

        return key

    def _swap(self, i: int, j: int) -> None:
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
