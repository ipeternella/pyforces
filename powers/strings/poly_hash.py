"""
Module with polynomial hashing for strings.
"""


def str_poly_hash(s: str) -> int:
    """
    Hashes a str using a polynomimal fn in which each s[i] is mapped to an integer
    relative to 'a' using ascii codes (ord() function) starting at 1 (not zero to
    to avoid collisions due to zero multiplication). The hash function has the form:

    F(s) = s[i] + s[i + 1] * p ^ 1 + s[i + 2] * p ^ 2 + ...

    In which p is a randomly choosen prime and the values are modulo'd to avoid big ints.
    """
    digest, prime, mod = 0, 31, 10 ** 9 + 7
    prime_power = 1

    for ch in s:
        ch_int = ord(ch) - ord("a") + 1  # maps each ch to int relative to 'a' (starts at 1)
        digest += ch_int * prime_power
        prime_power *= prime

        digest %= mod  # to avoid big ints: modulo
        prime_power %= mod

    return digest
