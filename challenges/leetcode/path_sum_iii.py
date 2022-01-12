"""
Solution for LC#437: Path Sum III

https://leetcode.com/problems/path-sum-iii/
"""
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_subarray_targets(nums, target):
            s = 0
            count = 0

            for i in range(len(nums) - 1, -1, -1):
                s += nums[i]

                if s == target:
                    count += 1

            return count

        def dfs(node):
            nonlocal total

            if node is None:
                return

            if node.left is None and node.right is None:
                nodes.append(node.val)
                total += count_subarray_targets(nodes, targetSum)
                nodes.pop()

                return

            nodes.append(node.val)

            dfs(node.left)
            dfs(node.right)

            total += count_subarray_targets(nodes, targetSum)
            nodes.pop()

        nodes: List[int] = []
        total = 0
        dfs(root)

        return total
