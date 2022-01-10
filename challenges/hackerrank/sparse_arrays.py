"""
Solution for: Sparse Arrays

https://www.hackerrank.com/challenges/sparse-arrays/problem
"""
from __future__ import annotations

from collections import Counter
from typing import List


class TrieNode:
    size: int
    is_str: bool
    count: int
    paths: List[TrieNode]

    def __init__(self, size: int, count: int = 0) -> None:
        self.paths = [None] * size  # type: ignore
        self.is_str = False
        self.count = count


class Trie:
    root: TrieNode
    alphabet_size: int

    def __init__(self, alphabet_size: int = 26) -> None:
        self.root = TrieNode(alphabet_size)
        self.alphabet_size = alphabet_size

    def add(self, s: str) -> None:
        curr = self.root

        for i in range(len(s)):
            j = ord(s[i]) - ord("a")

            if curr.paths[j] is None:
                curr.paths[j] = TrieNode(self.alphabet_size)

            curr = curr.paths[j]

        curr.is_str = True
        curr.count += 1  # same str insertion: increments count

    def count_matches(self, s: str) -> int:
        curr = self.root

        for i in range(len(s)):
            j = ord(s[i]) - ord("a")

            if curr.paths[j] is None:
                return 0

            curr = curr.paths[j]

        return curr.count


def matchingStringsWithTrie(strings: List[str], queries: List[str]) -> List[int]:
    """
    Answer using an adapted Trie for practicing purposes.
    """
    trie = Trie()
    for s in strings:
        trie.add(s)

    return [trie.count_matches(q) for q in queries]


def matchingStrings(strings: List[str], queries: List[str]) -> List[int]:
    """
    Straightforward answer.
    """
    freqs = Counter(strings)
    return [freqs[q] for q in queries]


if __name__ == "__main__":
    n = int(input().strip())
    strings = [input() for _ in range(n)]

    q = int(input().strip())
    queries = [input() for _ in range(q)]

    print("\n".join(map(str, matchingStrings(strings, queries))))
