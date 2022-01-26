"""
Module with a few bitwise operations.
"""


def update_bit_range(n: int, i: int, j: int, m: int) -> int:
    clear_mask = ~0 << (j + 1) | ~(~0 << i)
    return (n & clear_mask) | m << i


def clear_range_bits(n: int, i: int, j: int) -> int:
    # clears [i .. j] (inclusive) bits with 0-based indexing (right to left, ex: .. 4 3 2 1 0)
    mask = ~0 << (j + 1) | ~(~0 << i)
    return mask & n


def clear_last_bits(n: int, amount: int) -> int:
    # clears amount of bits from right to left <--
    mask = ~0 << amount
    return mask & n


def update_ith_bit(n: int, i: int, new_bit: int) -> int:
    if new_bit == 1:
        return set_ith_bit(n, i)

    return clear_ith_bit(n, i)


def set_ith_bit(n: int, i: int) -> int:
    mask = 1 << i
    return n | mask  # aligns the 1 bit with and OR op that will set that target to 1 (OR operation)


def clear_ith_bit(n: int, i: int) -> int:
    mask = ~(1 << i)  # shift 1 to the right bit position and negate it to have, ex: 111_0_11
    return mask & n


def get_ith_bit(n: int, i: int) -> int:
    mask = 1 << i  # shift 1 to the right bit position
    return 1 if mask & n > 0 else 0


def is_odd(n: int) -> bool:
    return n & 1 == 1


def is_power_of_two(n: int) -> bool:
    if n == 0:
        return False

    # 8 (1000) & 7 (0111) == 0000 (0)
    return n & (n - 1) == 0


def count_set_bits(n: int) -> int:
    # counts bits that are 1
    # O(log(N)) -> ex: n = 16 (2^4) has log16 ~ 4 bits to check
    # number N has ~ 2^N
    counter = 0
    while n:
        counter += n & 1
        n >>= 1

    return counter


10 ^ 8


def int_to_binary(n: int) -> int:
    # returns an integer compose only for the digits 1 and 0 (but as an int)
    # 9 (1001) --> 1 + 10^3 = 1001 (decimal which represents an int)
    binary = 0
    pow10 = 1
    while n:
        binary += (n & 1) * pow10
        pow10 *= 10
        n >>= 1

    return binary


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
