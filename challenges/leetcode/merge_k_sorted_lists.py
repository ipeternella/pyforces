"""
Solution for LC#23: Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/
"""
import itertools
import sys
from queue import PriorityQueue
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
        nodes = [root for root in lists if root is not None]
        new_nodes = []
        root = None
        is_root = True
        q = PriorityQueue()
        prev = None

        while nodes:
            next_min_val = INF
            for node in nodes:
                q.put((node.val, next(counter), node))  # counter: tiebreaker for nodes with same value (same priority)
                if node.next is not None:
                    next_min_val = min(next_min_val, node.next.val)

            # empty queue: no linked list nodes were added so all linked lists were traversed
            if q.empty():
                return root

            # prepare new root
            if is_root:
                _, _, root = q.get()
                is_root = False
                prev = root
                new_nodes.append(prev.next)

            while not q.empty():
                _, _, curr = q.get()

                if curr.val > next_min_val:
                    new_nodes.append(curr)
                else:
                    new_nodes.append(curr.next)
                    prev.next = curr  # type: ignore
                    prev = curr

            nodes = [node for node in new_nodes if node is not None]
            new_nodes = []

        return root
