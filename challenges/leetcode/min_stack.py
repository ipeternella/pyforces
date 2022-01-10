"""
Solution for LC#155: Min Stack

https://leetcode.com/problems/min-stack/submissions/
"""


class MinStack:
    def __init__(self):
        self.values = []  # LIFO of values
        self.min_values = []  # LIFO of mins

    def push(self, val: int) -> None:
        self.values.append(val)

        # [!]: push if val == min, too!
        if self.min_values and val <= self.min_values[-1]:
            self.min_values.append(val)

        if not self.min_values:
            self.min_values.append(val)

    def pop(self) -> None:
        val = self.values[-1]
        last_min = self.min_values[-1]

        if val == last_min:
            self.min_values.pop()

        return self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
