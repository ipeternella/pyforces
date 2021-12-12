"""
Module with segment trees also known as statistic trees. A segment tree contains nodes
in which node holds a statistic info regarding some intervals (segments). It can be built
in O(NlogN) and allows querying info from intervals in O(logN + K) where K is the number of intervals.


# (l, r) -> from [left, right] is the query range

# partial overlap -> go to the right and the left and return sum
# total overlap -> return value
# no overlap -> return "0"
"""
from typing import Callable
from typing import Generic
from typing import List
from typing import TypeVar

T = TypeVar("T")


class SegmentTree(Generic[T]):
    stree: List[T]
    values: List[T]
    statistic_fn: Callable

    def __init__(self, values: List[T], statistic_fn: Callable) -> None:
        self.statistic_fn = statistic_fn  # type: ignore
        self.stree = [None] * (4 * len(values))  # type: ignore
        self.values = values
        self._build(0, len(values) - 1, 0)

    def _build(self, start: int, end: int, node_i: int) -> None:
        # divide and conquer: leaf nodes just contain the bare values
        if start >= end:
            self.stree[node_i] = self.values[start]
            return

        mid = (start + end) // 2  # defines segments of the tree
        self._build(start, mid, 2 * node_i + 1)  # left child
        self._build(mid + 1, end, 2 * node_i + 2)  # right child

        self.stree[node_i] = self.statistic_fn((self.stree[2 * node_i + 1], self.stree[2 * node_i + 2]))

    def query(self, left: int, right: int):
        def _query(start: int, end: int, left: int, right: int, node_i: int):
            pass

        return _query(0, len(self.values) - 1, left, right, 0)
