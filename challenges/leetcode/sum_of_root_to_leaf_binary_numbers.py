"""
Solution for LC#1022: Sum of Root To Leaf Binary Numbers

https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if node is None:
                return 0

            # pre-order traversal: shift to make room for new val
            num <<= 1
            num |= node.val

            if node.left is None and node.right is None:
                return num

            sum_left = dfs(node.left, num)
            sum_right = dfs(node.right, num)
            num >>= 1  # "unshift" previously added num

            return sum_left + sum_right

        return dfs(root, 0)
