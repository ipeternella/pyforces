"""
Solution for: Encryption

https://www.hackerrank.com/challenges/encryption/problem
"""
import math
from io import StringIO


def encryption(s: str) -> str:
    s = "".join(s.split())
    str_builder = StringIO()
    l = len(s)
    l_root = len(s) ** 0.5
    r = math.floor(l_root)
    c = math.ceil(l_root)

    # r * c >= L
    while r * c < l:
        if r < c:
            r += 1
        else:
            c += 1

    a = [[""] * c for _ in range(r)]
    cursor = 0
    for i in range(r):
        for j in range(c):
            a[i][j] = s[cursor]
            cursor += 1

            if cursor >= l:
                break

    for j in range(c):
        for i in range(r):
            str_builder.write(a[i][j])

        if j != c - 1:
            str_builder.write(" ")

    return str_builder.getvalue()


if __name__ == "__main__":
    print(encryption(input()))
