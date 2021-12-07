from typing import List


def swap(arr: List, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def find_permutations(s: str) -> List[str]:
    """
    Finds all permutations of chars of a string. In a permutation, order matters.
    """
    n = len(s)
    chars = [ch for ch in s]  # necessary as strs are immutable!
    permutations: List[str] = []

    def backtrack_permutations(i: int, chars: List[str]):
        if i == n - 1:
            permutations.append("".join(chars.copy()))
            return

        for j in range(i, n):
            swap(chars, i, j)
            backtrack_permutations(i + 1, chars)
            swap(chars, i, j)  # backtracK: unswap

    backtrack_permutations(0, chars)
    return permutations
