"""
Solution for: Making Anagrams.

https://www.hackerrank.com/challenges/making-anagrams/problem
"""
from collections import Counter
from typing import Set


def makingAnagrams(s1: str, s2: str) -> int:
    c1 = Counter(s1)
    c2 = Counter(s2)
    popped: Set[str] = set()
    deletes = 0

    # if ch in s1 and not in s2 or freq differs: must be deleted
    for ch in c1:
        if ch in c2 and c2[ch] != c1[ch]:
            deletes += abs(c2[ch] - c1[ch])
        elif ch not in c2:
            deletes += c1[ch]

        popped.add(ch)

    # whatever is in s2 (not in popped) must still be deleted as they diverge from s1
    for ch in c2:
        if ch not in popped:
            deletes += c2[ch]

    return deletes


if __name__ == "__main__":
    print(makingAnagrams(input(), input()))
