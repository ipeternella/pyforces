"""
Solutions from LC#21: Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2, prev, list3):
            if not node1 and not node2:
                return list3

            # pick smallest value to merge
            if not node2:
                smallest = node1.val
                node1 = node1.next if node1 else None
            elif not node1:
                smallest = node2.val
                node2 = node2.next if node2 else None
            else:
                if node1.val <= node2.val:
                    smallest = node1.val
                    node1 = node1.next if node1 else None
                else:
                    smallest = node2.val
                    node2 = node2.next if node2 else None

            # build new node and make previous point to it
            node3 = ListNode(smallest)
            if not prev:
                list3 = node3  # head of the new lis
            else:
                prev.next = node3

            return merge(node1, node2, node3, list3)

        return merge(list1, list2, None, None)
