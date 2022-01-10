"""
Solution for LC#141: Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def move(node, steps=1):
    if node is None:
        return None

    node = node.next
    if steps == 1:
        return node

    if node is not None:
        return node.next

    return None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = move(head, steps=1)
        fast = move(head, steps=2)

        while fast is not None:  # if fast reaches the end (is None) there's no cycle!
            slow = move(slow, steps=1)
            fast = move(fast, steps=2)

            if slow == fast:  # slow has caught up with fast: cycle!
                return True

        return False
