"""
Solution for: New Year Chaos

https://www.hackerrank.com/challenges/new-year-chaos/problem
"""
from typing import List


def minimumBribes(q: List[int], n: int) -> int:
    bribes = 0
    missing = -1  # -1 represents a missing person when someone advances two positions ahead

    for i, person in enumerate(q):
        shift = person - (i + 1)  # shifted position of the current person in the queue

        if shift > 2:
            return -1  # Too chaotic: person advanced too much
        elif shift == 2 and missing == -1:
            missing = i + 1  # person took place of the (i + 1) person, who's now missing
            bribes += 2
        elif shift == 2 and missing != -1:
            bribes += 2  # keep looking for missing person until a shift < 2 is found
        elif missing != -1:
            if person > missing:  # after 2-shift, if the person found is > missing: extra bribe
                bribes += 1
            missing = -1
        elif shift == 1:
            bribes += 1

    return bribes


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        rslt = minimumBribes(q, n)

        print(rslt) if rslt >= 0 else print("Too chaotic")
