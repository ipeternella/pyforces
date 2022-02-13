"""
Module with code to handle problems with huge/exponential solution spaces such as computing:

- Subsets
- Permutations
- Combinations

The solutions covered here make use of backtracking algorithms to search the whole
solution space.
"""
from typing import List


def subsets(s: str) -> List[str]:
    """
    Finds all subsets of chars of a given string. A subset does not need to maintain an
    order nor continuity of the data.

    Subsets are created by either picking or NOT picking each item of the array or string. It
    includes the null set (empty list or string).

    Search space size: 2^N (pick or not each item)

    Example:
        "abc" -> ["abc", "ab", "ac", "bc", "c", "a", "b", ""] where N == 3, so 2^3 solutions (includes null set - "")
    """

    def backtrack(start, subset):
        if start > n - 1:
            subsets.append("".join(subset))
            return

        # path 1: pick the item
        subset.append(s[start])
        backtrack(start + 1, subset)

        # path 2: backtrack and do not pick the item
        subset.pop()
        backtrack(start + 1, subset)

    n = len(s)
    subsets = []

    # to generate subsets: either pick the item or not: 2^n possibilities
    backtrack(0, [])
    return subsets


def permutations(s: str) -> List[str]:
    """
    Finds all permutations of chars of a string. In a permutation, order matters.

    Permutations are created by picking each item of an array or string and combining it with
    every other remaining item. The code for permutations includes swapping elements of the array
    in order to pick each item with every other possible remaining item.

    Search space size: N! (if N == 3, then 3 * 2 * 1 permutations do exist).

    Example:
        "abc" -> ["abc", "acb", "bac", "bca", "cab", "cba"]  where N == 3, so 3! solutions
    """

    def backtrack(i: int, chars: List[str]):
        if i == n - 1:
            permutations.append("".join(chars.copy()))
            return

        for j in range(i, n):
            chars[i], chars[j] = chars[j], chars[i]  # swap
            backtrack(i + 1, chars)
            chars[i], chars[j] = chars[j], chars[i]  # backtrack: unswap

    n = len(s)
    chars = [ch for ch in s]  # necessary as strs are immutable!
    permutations: List[str] = []

    backtrack(0, chars)
    return permutations
