"""
Solution for LC#144: Binary Tree Preorder Traversal

https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from collections import deque as Queue
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q: Queue[TreeNode] = Queue()
        stack = []
        nodes = []

        if root is not None:
            q.append(root)

        # bfs with stack to go back to right nodes
        while q:
            node = q.popleft()
            nodes.append(node.val)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                stack.append(node.right)

            if not q and stack:
                q.append(stack.pop())

        return nodes


class SolutionTrivial:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def dfs(node):
            if node is None:
                return

            nodes.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return nodes
