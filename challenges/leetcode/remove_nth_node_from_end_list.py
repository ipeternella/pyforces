"""
Solution for LC#19: Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes: List[Optional[ListNode]] = [head]
        current = head

        while current is not None:
            current = current.next

            if current is not None:
                nodes.append(current)

        sz = len(nodes)
        nth_node = nodes[sz - n]
        prev_node = nodes[sz - n - 1] if sz - n - 1 >= 0 else None
        next_node = nodes[sz - n + 1] if sz - n + 1 <= sz - 1 else None

        # removing the head
        if prev_node is None:
            head = nth_node.next  # type: ignore
        elif next_node is None:  # last node of the list
            prev_node.next = None
        else:
            prev_node.next = next_node

        nth_node.next = None  # type: ignore
        return head
