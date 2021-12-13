"""
Solution for: Contacts

https://www.hackerrank.com/challenges/contacts/problem
"""
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.paths = [None] * 26
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, partial: str) -> None:
        curr = self.root

        for ch in partial:
            j = ord(ch) - ord("a")

            if curr.paths[j] is None:
                curr.paths[j] = TrieNode()

            curr = curr.paths[j]
            curr.counter += 1

    def count_contacts(self, partial: str) -> int:
        curr = self.root

        for i, ch in enumerate(partial):
            j = ord(ch) - ord("a")

            if curr.paths[j] is None:
                return 0

            curr = curr.paths[j]

        return curr.counter


def contacts(queries: List[List[str]]) -> List[int]:
    trie = Trie()
    counts = []

    for op, partial in queries:
        if op == "add":
            trie.add(partial)
        else:
            counts.append(trie.count_contacts(partial))

    return counts


if __name__ == "__main__":
    n = int(input().strip())
    queries = [input().rstrip().split() for _ in range(n)]

    print("\n".join(map(str, contacts(queries))))
