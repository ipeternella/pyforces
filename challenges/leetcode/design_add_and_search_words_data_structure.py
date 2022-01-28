"""
Solution for LC#211: Design Add and Search Words Data Structure

https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class TrieNode:
    def __init__(self, ch=None):
        self.char = ch
        self.next = [None] * 26
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def _char_index(self, ch: str) -> int:
        return ord(ch) - ord("a")

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            i = self._char_index(ch)
            if node.next[i] is None:
                node.next[i] = TrieNode(ch)

            node = node.next[i]

        node.is_end = True

    def search(self, word: str) -> bool:
        return self._search(self.root, word, 0)  # recursive solution for ". searches"

    def _search(self, node: TrieNode, word: str, i: int) -> bool:
        n = len(word)
        if i == n:
            return node.is_end  # check if it's a word or not

        ch = word[i]
        char_i = self._char_index(ch)

        if ch == ".":
            # ". (matches any) search": traverse every non-empty next node of the current node
            for node in node.next:
                if node:
                    if self._search(node, word, i + 1):  # recurse to next char
                        return True

            return False  # if all nodes fail or are empty: nothing was found

        if node.next[char_i]:
            return self._search(node.next[char_i], word, i + 1)

        return False
