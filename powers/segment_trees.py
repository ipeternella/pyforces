"""
Module with segment (statistic trees). A segment tree contains nodes in which each node
holds a statistic info that aggregates info of some intervals (segments) of a list of values.

Tree can be built in O(NlogN) and allows querying info from intervals in O(logN + K)
where K is the number of intervals.
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

    def _build(self, start: int, end: int, tree_i: int) -> None:
        # divide and conquer: leaf nodes just contain the bare values
        if start >= end:
            self.stree[tree_i] = self.values[start]
            return

        mid = (start + end) // 2  # defines segments of the tree
        self._build(start, mid, 2 * tree_i + 1)  # left child
        self._build(mid + 1, end, 2 * tree_i + 2)  # right child

        # parent
        self.stree[tree_i] = self.statistic_fn((self.stree[2 * tree_i + 1], self.stree[2 * tree_i + 2]))

    def query(self, left: int, right: int):
        def _query(node_start: int, node_end: int, tree_i: int):
            if node_start > right or node_end < left:  # no segment overlapping
                return 0

            if node_start >= left and node_end <= right:  # full segment overlap
                return self.stree[tree_i]

            # partial segment overlap
            mid = (node_start + node_end) // 2
            query_1 = _query(node_start, mid, 2 * tree_i + 1)
            query_2 = _query(mid + 1, node_end, 2 * tree_i + 2)

            return self.statistic_fn((query_1, query_2))

        return _query(0, len(self.values) - 1, 0)

    def update(self, i: int, new_value: T) -> None:
        def _update(node_start: int, node_end: int, tree_i: int):
            # base case
            if node_start == node_end:
                self.stree[tree_i] = new_value
                return

            mid = (node_start + node_end) // 2
            if i <= mid:
                _update(node_start, mid, 2 * tree_i + 1)
            else:
                _update(mid + 1, node_end, 2 * tree_i + 2)

            # aggregate parent node using statistic fn
            left_child = self.stree[2 * tree_i + 1]
            right_child = self.stree[2 * tree_i + 2]
            self.stree[tree_i] = self.statistic_fn((left_child, right_child))

        _update(0, len(self.values) - 1, 0)
