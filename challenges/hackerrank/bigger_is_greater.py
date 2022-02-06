"""
Solution for: Bigger is Greater

https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""
import heapq
import os
import sys


def main():
    t = int(input())

    for _ in range(t):
        w = [ch for ch in input()]
        n = len(w)
        permuted = False
        ans = ""
        heap = []  # min.heap for storing candidates for first swap point

        # start with the last char to go from right to left of w
        prev = w[n - 1]
        heapq.heappush(heap, (ord(w[n - 1]), n - 1))  # heap: [(char_code, index), (97, 10), ...]

        for i in range(n - 2, -1, -1):
            ch = w[i]
            ch_code = ord(ch)

            if ch_code < ord(prev):
                ch2_code = 0
                ch2_i = 0

                # look in the heap for the smallest char that's bigger than current char
                while heap:
                    ch2_code, ch2_i = heapq.heappop(heap)
                    if ch2_code > ch_code:  # found smallest from heap that's bigger than current char
                        break

                # make the first swap: guarantees a bigger permutation
                w[i], w[ch2_i] = w[ch2_i], w[i]

                # sort the rest of w after the swap point to get the smallest
                # permutation that's also bigger than w (guaranteed by first swap)
                ans = w[: i + 1] + sorted(w[i + 1 : n])
                ans = "".join(ans)
                permuted = True
                break
            else:
                prev = ch
                heapq.heappush(heap, (ch_code, i))

        if permuted:
            print(ans)
        else:
            print("no answer")


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
