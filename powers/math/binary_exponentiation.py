"""
Module with an efficient approach to compute exponentiations.
"""


# [!]: runs in O(log(b)): so for 10^18 it runs ~ 64 ops and not 10^18 ops [!]
def power(a: int, b: int) -> int:
    """
    Given a base a = 3 and exponent b = 5 we want to compute: 3 ^ 5.
    Start by decomposing such exponentiation into powers of 2: _1_, 2, _4_, 8, 16, so:
        - 3^5 = 3^4 * 3^1

    As such, we can use the set bits of the exponent b = 5 (101) to compute a ^ b in log(b):
    - For every set bit of b: ans *= a
    - Always increase a *= a
    - For next set bit of b: ans *= a will give the decomposed exponentation: ans = 3^1 * 3^4
    """
    ans = 1
    while b:
        if b & 1:  # for every set bit, multiply b by the powered a
            ans *= a

        a *= a
        b >>= 1

    return ans
