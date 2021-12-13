import unittest

from parameterized import parameterized

from powers.strings.pattern_matching_bruteforce import matches_pattern


class PatternMatchingBruteForceTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("ababaababbbbabaaa", "aa", True),
            ("ababaababbbbabaaa", "zb", False),
        ]
    )
    def test_should_find_pattern(self, text, pattern, expected_has_match):
        # act
        has_match = matches_pattern(text, pattern)

        # assert
        self.assertEqual(has_match, expected_has_match)
