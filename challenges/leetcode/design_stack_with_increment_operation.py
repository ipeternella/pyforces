"""
Solution for LC#1381: Design a Stack With Increment Operation

https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""


class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()

        return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        for i in range(k):
            self.stack[i] += val
