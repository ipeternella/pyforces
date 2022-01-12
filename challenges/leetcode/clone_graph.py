"""
Solution for LC#133: Clone Graph

https://leetcode.com/problems/clone-graph/
"""
from typing import List
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def dfs(v):
            visited[v.val] = True
            new_v = Node(v.val)
            nodes[v.val] = new_v

            for adj_v in v.neighbors:
                if not visited[adj_v.val]:
                    dfs(adj_v)

                adj_ref = nodes[adj_v.val]
                new_v.neighbors.append(adj_ref)

        if node is None:
            return None

        # key space: 1 <= node.val <= 100 (101 indexes)
        nodes: List[Optional["Node"]] = [None] * 101
        visited = [False] * 101

        dfs(node)
        return nodes[node.val]
