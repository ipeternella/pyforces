from typing import List
from typing import Tuple


def find_subarray_sums(nums: List[int], target: int) -> List[Tuple[int, int]]:
    n = len(nums)
    if n < 1:
        return []

    i, j = 0, 0
    s = nums[i]
    subarrays = []

    # two pointers
    while j < n and i < n:
        if s == target:
            subarrays.append((i, j))
            s -= nums[i]
            i += 1
        elif j + 1 < n and s + nums[j + 1] <= target:
            j += 1
            s += nums[j]
        else:
            s -= nums[i]
            i += 1

    return subarrays
