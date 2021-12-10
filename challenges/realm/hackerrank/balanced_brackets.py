"""
Solution for: Balanced Brackets

https://www.hackerrank.com/challenges/balanced-brackets/problem
"""
from typing import List


def isBalanced(s: str) -> bool:
    brackets = {")": "(", "}": "{", "]": "["}  # dict[closing_bracket] <- opening_bracket
    open_brackets_stack: List[str] = []

    for bracket in s:
        if bracket not in brackets:  # opening bracket
            open_brackets_stack.append(bracket)
        elif bracket in brackets and not open_brackets_stack:  # closing bracket without opening bracket
            return False
        else:  # closing bracket with previous opening bracket
            last_open_bracket = open_brackets_stack.pop()
            expected_open_bracket = brackets[bracket]

            if last_open_bracket != expected_open_bracket:
                return False

    return len(open_brackets_stack) == 0  # no left opening brackets


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        print("YES") if isBalanced(input()) else print("NO")
