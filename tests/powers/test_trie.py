import unittest

from powers.strings.trie import Trie


class TrieTests(unittest.TestCase):
    def test_should_search_and_find_strings_in_trie(self):
        # arrange
        trie = Trie()

        # act
        trie.add("abc")
        trie.add("aabc")
        trie.add("ccba")

        # assert - full strs
        self.assertTrue("abc" in trie)
        self.assertTrue("aabc" in trie)
        self.assertTrue("ccba" in trie)

        # assert - prefixes that do not make up the full strings
        self.assertFalse("bc" in trie)
        self.assertFalse("cc" in trie)
        self.assertFalse("cba" in trie)
