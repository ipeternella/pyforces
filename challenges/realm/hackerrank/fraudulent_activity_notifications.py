"""
Hackerrank solution for Fraudulent Activity Notifications:

https://www.hackerrank.com/challenges/fraudulent-activity-notifications

Topics: countsort, linear median finding
"""

from typing import List


def get_frequencies(nums: List[int], start: int, end: int, k: int) -> List[int]:
    # just grab frequencies of the nums much like the first step of countsort
    freq = [0] * (k + 1)

    for i in range(start, end + 1):
        freq[nums[i]] += 1

    return freq


def update_frequencies(frequencies: List[int], old: int, new: int) -> None:
    frequencies[old] -= 1
    frequencies[new] += 1


def median_from_frequency(frequencies: List[int], d: int) -> float:
    # uses frequencies of nums to compute the median value in order to avoid ~ O(N) of countsorting
    s = 0
    target = 0

    if d % 2 == 0:
        target = d // 2
        has_lower_median = False

        for i, freq in enumerate(frequencies):
            if has_lower_median:
                if freq == 0:
                    continue
                else:
                    upper_median = i
                    break

            s += freq

            if s == target:
                lower_median = i
                has_lower_median = True
                continue

            elif s > target:  # repeated elements (lower and upper median are the same)
                return i

        return (lower_median + upper_median) / 2

    # odd medians
    target = d // 2 + 1
    for i, freq in enumerate(frequencies):
        s += freq

        if s >= target:
            return float(i)

    return 0.0


def activityNotifications(expenditure: List[int], d: int) -> int:
    n = len(expenditure)
    m = 0.0
    k = 200
    freqs: List[int] = []

    # O(N) as d <= N
    freqs = get_frequencies(expenditure, 0, d - 1, k)
    m = median_from_frequency(freqs, d)
    notifications = 1 if expenditure[d] >= 2 * m else 0

    # O(N*k)
    for i in range(d + 1, n):
        update_frequencies(freqs, expenditure[i - d - 1], expenditure[i - 1])
        m = median_from_frequency(freqs, d)  # O(k)

        if expenditure[i] >= 2 * m:
            notifications += 1

    return notifications
