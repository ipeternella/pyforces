"""
Solution for: Missing Numbers

https://www.hackerrank.com/challenges/missing-numbers/problem
"""
from collections import Counter
from typing import List


def missingNumbers(a: List[int], b: List[int]) -> List[int]:
    counter_b = Counter(b)
    counter_a = Counter(a)
    missing = set()

    for num in b:
        if num not in counter_a:
            missing.add(num)

        if num in counter_a and counter_a[num] != counter_b[num]:
            missing.add(num)

    return sorted(list(missing))


if __name__ == "__main__":
    n = input().strip()
    a = [int(num) for num in input().split()]
    m = input().strip()
    b = [int(num) for num in input().split()]

    print(" ".join(map(str, missingNumbers(a, b))))
