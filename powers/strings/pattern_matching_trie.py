"""
Pattern matching strings with Tries for better running times.

Works by building up a Trie with all the suffixes of the text and then searching
the pattern as a prefix.
"""
from powers.strings.trie import Trie


def matches_pattern(text: str, pattern: str) -> bool:
    n = len(text)

    # Trie of suffixes
    trie = Trie()

    # O(N^2) ~ N + (N - 1) + (N - 2) + ... (triangular numbers -> sum = n(n + 1)/2 )
    for i in range(n):
        trie.add(text[i:])

    # search for the ptrn as a prefix in the Trie
    # O(|pattern|) but the insertion is O(N^2) -> other alternatives: KMP, Z-algorithm, etc.
    return trie.contains_prefix(pattern)
