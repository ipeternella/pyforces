"""
Module with binary tree traversal examples. For simplicity, the traversals just
print the nodes which can be easily test my mocking the built-in print function.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


def bfs(node: Optional[TreeNode]) -> None:
    """
    Breadth-first traversal of binary trees.
    """
    if node is None:
        return

    q: Deque[TreeNode] = deque()
    q.append(node)

    while q:
        current_node: TreeNode = q.popleft()  # FIFO
        adjacent = [current_node.left, current_node.right]

        print(current_node.val)

        # bfs
        for adj_node in adjacent:
            if adj_node is not None:  # current node might not have children
                q.append(adj_node)


def dfs_inorder(node: Optional[TreeNode]) -> None:
    """
    Depth-first search in-order traversal of binary trees.

    Uses:
        - traverses nodes in an INCREASING order in binary search trees.
        - swapping left with right: traverses in DECREASING order
    """
    if node is None:
        return

    dfs_inorder(node.left)
    print(node.val)  # in-order name due to BSTrees: left < node < right
    dfs_inorder(node.right)


def dfs_preorder(node: Optional[TreeNode]) -> None:
    r"""
    Depth-first search pre-order traversal of binary trees.

    Uses:
        - copy the tree
        - get a prefix expression from an expression tree:
              +
             / \
            2   3  --> (+ 2 3)
    """
    if node is None:
        return

    print(node.val)  # root comes first -> pre-order
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_postorder(node: Optional[TreeNode]) -> None:
    r"""
    Depth-first search post-order traversal of binary trees. It
    traverses all nodes on the same level and then moves up.

    Uses:
        - traverse node on the same level before moving up
        - delete the tree (removes nodes on same level)
        - get a postfix expression from an expression tree:
              +
             / \
            2   3  --> (2 3 +)
    """
    if node is None:
        return

    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.val)
