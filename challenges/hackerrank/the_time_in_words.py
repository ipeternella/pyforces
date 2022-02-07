"""
Solution for: The Time In Words

https://www.hackerrank.com/challenges/the-time-in-words/problem
"""
import os
import sys

num_words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
]


def minutes(m):
    if 21 <= m < 30:
        return num_words[20] + " " + num_words[m - 20]

    return num_words[m]


def main():
    h = int(input())
    m = int(input())

    if m == 0:
        print(f"{num_words[h]} o' clock")
    elif 1 <= m <= 30:
        minutes_word = "minute" if m == 1 else "minutes"

        if m == 15:
            print(f"quarter past {num_words[h]}")
        elif m == 30:
            print(f"half past {num_words[h]}")
        else:
            print(f"{minutes(m)} {minutes_word} past {num_words[h]}")
    else:
        next_hour = h + 1 if h + 1 <= 12 else 1
        remaining_mins = 60 - m
        minutes_word = "minute" if remaining_mins == 1 else "minutes"

        if m == 45:
            print(f"quarter to {num_words[next_hour]}")
        else:
            print(f"{minutes(remaining_mins)} {minutes_word} to {num_words[next_hour]}")


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
