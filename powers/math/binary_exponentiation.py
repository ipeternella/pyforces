"""
Module with an efficient approach to compute exponentiations.
"""


def power(a: int, b: int) -> int:
    # [!]: runs in O(log(b)): so for 10^18 it runs ~ 64 ops and not 10^18 ops [!]

    # decompose the exponent b into bases of 2, e.g., 5 == 4 + 1 (2^2 + 2^0)
    # such decomposition matches the set bits of b: 5 == b101
    # so for every set bit of b we multiply the rslt by a which will have powers of 2
    rslt = 1
    while b:
        if b & 1:
            rslt *= a  # a == 3^1 then 3^4 when computing 3^5 (a == 3, b == 5)

        a *= a
        b >>= 1

    return rslt


def mod_power(a: int, b: int, mod: int = 1000000007) -> int:
    rslt = 1
    while b:
        if b & 1:
            rslt *= a
            rslt %= mod  # (rslt * a) % mod == rslt * a if (rslt * a) < mod

        a *= a
        a %= mod
        b >>= 1

    return rslt
