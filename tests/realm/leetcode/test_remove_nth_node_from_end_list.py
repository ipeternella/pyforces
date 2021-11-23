import unittest

from parameterized import parameterized

from challenges.realm.leetcode.remove_nth_node_from_end_list import Solution
from tests.support.leetcode.linked_lists import assert_leetcode_linked_list
from tests.support.leetcode.linked_lists import build_linked_list


class RemoveNthNodeFromEndListTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
            ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ]
    )
    def test_should_remove_nth_node_from_linkedlist(self, linked_list, n, expected_linked_list):
        # arrange
        head = build_linked_list(linked_list)

        # act
        head = self.solution.removeNthFromEnd(head, n)

        # assert
        assert_leetcode_linked_list(head, expected_linked_list)
