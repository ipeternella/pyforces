"""
Solution for LC#657: Robot Return to Origin

https://leetcode.com/problems/robot-return-to-origin/
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        for move in moves:
            if move == "L":
                x -= 1
            elif move == "R":
                x += 1
            elif move == "U":
                y += 1
            else:
                y -= 1

        return (x, y) == (0, 0)
