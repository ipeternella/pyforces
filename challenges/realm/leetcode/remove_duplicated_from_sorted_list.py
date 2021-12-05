"""
Solution for LC#83: Remove Duplicates from Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        nxt = head.next

        while curr is not None:
            if nxt and nxt.val == curr.val:
                curr.next = nxt.next  # do not advance in the list: check for more duplicates
            else:
                curr = curr.next
            nxt = curr.next if curr else None

        return head
