"""
Solution for LC#1302: Deepest Leaves Sum

https://leetcode.com/problems/deepest-leaves-sum/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    deepest_sum = 0
    tree_height = 0

    def height(self, root) -> int:
        if not root:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def dfs(self, root: Optional[TreeNode], level: int = 1) -> None:
        if not root:
            return

        # leaf
        if not root.left and not root.right:
            if level == self.tree_height:
                self.deepest_sum += root.val

        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.tree_height = self.height(root)
        self.deepest_sum = 0
        self.dfs(root)

        return self.deepest_sum
