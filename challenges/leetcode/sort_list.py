"""
Solution for LC#148: Sort List

https://leetcode.com/problems/sort-list/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity: O(N*logN), Space complexity: O(1)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mid(head):
            slow = head
            fast = head.next

            while fast:
                slow = slow.next
                fast = fast.next.next if fast.next is not None else None

            return slow

        def merge(h1, h2):
            curr1 = h1
            curr2 = h2

            while curr1 and curr2:
                tmp = None
                prepend_list1 = curr2.val >= curr1.val

                if prepend_list1:
                    while curr2.val >= curr1.val:
                        if curr1.next is None or curr1.next.val > curr2.val:
                            tmp = curr1.next
                            break

                        curr1 = curr1.next

                    curr1.next = curr2
                    curr1 = tmp  # can be None

                if curr1:
                    while curr2.val <= curr1.val:
                        if curr2.next is None or curr2.next.val > curr1.val:
                            tmp = curr2.next
                            break

                        curr2 = curr2.next

                    curr2.next = curr1
                    curr2 = tmp  # can be None

            return h1 if h1.val <= h2.val else h2

        def mergesort(head):
            if head is None:
                return None

            if head.next is None:
                return head  # list of a single node

            center = mid(head)
            center_next = center.next

            # break the list in two halves
            if center_next:
                center.next = None
            else:
                # list with two elements
                center_next = head.next
                head.next = None

            left_head = mergesort(head)
            right_head = mergesort(center_next)

            return merge(left_head, right_head)  # merge two sorted linked lists

        return mergesort(head)
