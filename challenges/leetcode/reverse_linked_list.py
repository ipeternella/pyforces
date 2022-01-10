"""
Solutions from LC#206: Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node, new_head=None):
            if not node:
                return None, None

            if not node.next:
                return node, node  # found the new head: the last node

            node_ahead, new_head = helper(node.next, new_head)
            if node_ahead:
                node_ahead.next = node  # prev node
            if node == head:
                node.next = None

            return node, new_head

        _, new_head = helper(head)
        return new_head
