"""
Pattern matching in strings using bruteforce and substrings/slices.
"""


def matches_pattern(text: str, pattern: str) -> bool:
    n = len(text)
    m = len(pattern)

    # O(N^2) / O(NM)
    for i in range(n - m + 1):
        if text[i : (i + m)] == pattern:  # [start:end (not inclusive)]
            return True

    return False
