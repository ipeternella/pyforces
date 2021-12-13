"""
Module with trie structure made for str prefixes.
"""
from __future__ import annotations

from typing import List


class TrieNode:
    """
    Represents a node of a Trie structure.
    """

    size: int  # size of the paths for each node (alphabet size)
    is_str: bool  # whether or not this node builds up a str that was previously inserted
    paths: List[TrieNode]  # mapping of indexes (ord) to chars

    def __init__(self, size: int) -> None:
        self.paths = [None] * size  # type: ignore
        self.is_str = False


class Trie:
    """
    Represents a trie data structure.
    """

    root: TrieNode
    alphabet_size: int

    def __init__(self, alphabet_size: int = 26) -> None:
        self.root = TrieNode(alphabet_size)
        self.alphabet_size = alphabet_size

    def add(self, s: str) -> None:
        """
        Inserts a new string into the Trie of prefixes. Running time is O(|s|).
        """
        curr = self.root

        for i in range(len(s)):
            j = ord(s[i]) - ord("a")  # ix of the mapping on each node

            if curr.paths[j] is None:  # if the node of this prefix doesn't exist
                curr.paths[j] = TrieNode(self.alphabet_size)

            curr = curr.paths[j]

        curr.is_str = True

    def __contains__(self, s: str) -> bool:
        """
        Checks if a given string is in the Trie or not. Running time is O(|s|).
        """
        curr = self.root

        for i in range(len(s)):
            j = ord(s[i]) - ord("a")  # ix of the mapping on each node

            if curr.paths[j] is None:
                return False

            curr = curr.paths[j]

        return curr.is_str
