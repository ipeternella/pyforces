"""
Solution for: Queue using Two Stacks

https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""
from typing import List


class Queue:
    staging_stack: List[int]
    output_stack: List[int]

    def __init__(self) -> None:
        self.staging_stack = []
        self.output_stack = []

    def enqueue(self, x: int) -> None:
        self.staging_stack.append(x)

    def dequeue(self) -> int:
        if self.output_stack:
            return self.output_stack.pop()

        self._flush_staging()  # flush all values from the staging stack to the output in correct order
        if self.output_stack:  # there must elements in the output stack
            return self.output_stack.pop()

        return -1

    def peek(self) -> int:
        if self.output_stack:
            return self.output_stack[-1]

        return self.staging_stack[0]

    def _flush_staging(self) -> None:
        for _ in range(len(self.staging_stack)):
            self.output_stack.append(self.staging_stack.pop())


if __name__ == "__main__":
    q = Queue()

    for _ in range(int(input())):
        raw = input().rstrip().split()
        if len(raw) == 2:
            q.enqueue(int(raw[1]))
        elif raw[0] == "2":
            q.dequeue()
        else:
            print(q.peek())
