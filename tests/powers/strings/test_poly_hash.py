import unittest

from parameterized import parameterized

from powers.strings.poly_hash import str_poly_hash


class StrPolyHashTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("abababa", 945746110),
            ("ababa", 984127),
        ]
    )
    def test_should_poly_hash_string(self, s, expected_digest):
        # act
        digest = str_poly_hash(s)

        # assert
        self.assertEqual(digest, expected_digest)
