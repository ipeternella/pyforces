import unittest

from parameterized import parameterized

from powers.strings.pattern_matching_trie import matches_pattern


class PatternMatchingTrieTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("ababba", "aba", True),
            ("ababba", "abz", False),
        ]
    )
    def test_should_find_pattern(self, text, pattern, expected_has_match):
        # act
        has_match = matches_pattern(text, pattern)

        # assert
        self.assertEqual(has_match, expected_has_match)
