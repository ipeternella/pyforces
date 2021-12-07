from typing import List


def find_subsets(s: str) -> List[str]:
    """
    Finds all subsets of chars of a given string. A subset does not need to maintain an
    order nor continuity of the data.

    Example:
        "abc" -> ["abc", "ab", "ac", "bc", "c", "a", "b", ""]  # null set
    """

    buffer: List[str] = []
    subsets: List[str] = []
    n = len(s)

    def backtrack_subset(s: str, buffer: List[str], subsets: List[str], i: int):
        if i == n:
            subsets.append("".join(buffer))
            return

        buffer.append(s[i])
        backtrack_subset(s, buffer, subsets, i + 1)

        buffer.pop()
        backtrack_subset(s, buffer, subsets, i + 1)

    backtrack_subset(s, buffer, subsets, 0)
    return subsets
