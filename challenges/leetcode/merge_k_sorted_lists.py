"""
Solution for LC#23: Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/
"""
import heapq
import itertools
import sys
from typing import List
from typing import Optional

INF = sys.maxsize
counter = itertools.count()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = lists
        new_nodes = []
        root = None
        is_root = True
        min_heap = []
        prev = None

        while nodes:
            next_min_val = INF

            for node in nodes:
                if node is not None:
                    if node.next is not None:
                        next_min_val = min(next_min_val, node.next.val)
                    heapq.heappush(min_heap, (node.val, next(counter), node))

            # empty min. heap: no nodes were added so all linked lists were traversed
            if not min_heap:
                return root

            # prepare new root
            if is_root:
                _, _, prev = heapq.heappop(min_heap)
                root = prev
                is_root = False
                new_nodes.append(prev.next)  # advance list

            while min_heap:
                val, _, curr = heapq.heappop(min_heap)

                # only values that are smaller than the next min value are added in this iteration
                # and such list pointers are advanced! lists with bigger values are not advanced!
                if val > next_min_val:
                    new_nodes.append(curr)  # keep list as is
                else:
                    new_nodes.append(curr.next)  # advance list
                    prev.next = curr  # type: ignore
                    prev = curr

            nodes = new_nodes
            new_nodes = []

        return root
