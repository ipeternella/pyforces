"""
Solution for LC#160: Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def advance(node, k):
            while k > 0:
                node = node.next
                k -= 1

            return node

        def get_lengths(node_a, node_b):
            n, m = 0, 0
            while node_a or node_b:
                if node_a:
                    n += 1

                if node_b:
                    m += 1

                node_a = node_a.next if node_a else None
                node_b = node_b.next if node_b else None

            return n, m

        n, m = get_lengths(headA, headB)
        node_a, node_b = headA, headB

        if n > m:
            node_a = advance(node_a, n - m)
        else:
            node_b = advance(node_b, m - n)

        while node_a:
            if node_a == node_b:
                return node_a

            node_a, node_b = node_a.next, node_b.next

        return None
