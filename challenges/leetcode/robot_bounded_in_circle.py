"""
Solution for LC#1041: Robot Bounded In Circle

https://leetcode.com/problems/robot-bounded-in-circle/
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def rotate_left(d):
            left_rotations = {"up": "left", "left": "down", "down": "right", "right": "up"}
            return left_rotations[d]

        def rotate_right(d):
            right_rotations = {"up": "right", "right": "down", "down": "left", "left": "up"}
            return right_rotations[d]

        def count_move(d):
            nonlocal ups, downs, lefts, rights

            if d == "up":
                ups += 1
            elif d == "down":
                downs += 1
            elif d == "left":
                lefts += 1
            else:
                rights += 1

        ups, downs, lefts, rights = 0, 0, 0, 0
        direction = "up"

        # if the robot's instructions do not immediately form a cycle, then if such
        # instructions ever lead to one it will require 4x such instructions so
        # by repating the instructions 4 times the algorithm can detect cycles
        for move in instructions * 4:
            if move == "G":
                count_move(direction)
            elif move == "L":
                direction = rotate_left(direction)
            else:
                direction = rotate_right(direction)

        return ups == downs and lefts == rights
