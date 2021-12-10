import unittest

from parameterized import parameterized

from challenges.realm.hackerrank.making_anagrams import makingAnagrams


class MakingAnagramsTests(unittest.TestCase):
    @parameterized.expand(
        [("cde", "abc", 4), ("absdjkvuahdakejfnfauhdsaavasdlkj", "djfladfhiawasdkjvalskufhafablsdkashlahdfa", 19)]
    )
    def test_should_compute_deletes_for_anagram(self, s1, s2, expected_deletes_for_anagram):
        # act
        deletes_for_anagram = makingAnagrams(s1, s2)

        # assert
        self.assertEqual(deletes_for_anagram, expected_deletes_for_anagram)
