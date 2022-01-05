"""
Solution for LC#24: Swap Nodes in Pairs

https://leetcode.com/problems/swap-nodes-in-pairs/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        next_node = head.next if head is not None else None

        # linked lists with 0 or 1 nodes only
        if curr_node is None or next_node is None:
            return head

        while curr_node is not None and next_node is not None:
            if prev_node is not None:
                prev_node.next = next_node

            if curr_node == head:
                head = next_node

            # swap
            curr_node.next = next_node.next
            next_node.next = curr_node

            prev_node = curr_node
            curr_node = curr_node.next if curr_node is not None else None
            next_node = curr_node.next if curr_node is not None else None

        return head
