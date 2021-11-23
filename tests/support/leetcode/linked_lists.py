"""
Linked-list supporting functions for the tests.
"""

from typing import List
from typing import Optional


class ListNode:
    """
    LeetCode's linked list representation.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if len(values) == 0:
        return None

    head = ListNode(values[0], None)
    prev = head

    for val in values[1:]:
        new_node = ListNode(val, None)
        prev.next = new_node
        prev = new_node

    return head


def assert_leetcode_linked_list(head: Optional[ListNode], values: List[int]) -> None:
    if not values and head is not None:
        # no values, so head should be none
        raise AssertionError("Expected an empty linked list!")

    if values and head is None:
        # values exist, but head is none
        raise AssertionError("Expected a non-empty linked list!")

    node = head
    size = 1 if node is not None else 0

    while node is not None:
        try:
            rslt = node.val == values[size - 1]

            if rslt is False:
                raise AssertionError(f"Value {node.val} does not match expected value of: {values[size - 1]}")

        except IndexError:
            raise AssertionError("Size of the linked list and its expected values do not match!")

        node = node.next
        size += 1

    size -= 1  # extra from last iteration
    if size != len(values):
        raise AssertionError("Size of the linked list and its expected values do not match!")
