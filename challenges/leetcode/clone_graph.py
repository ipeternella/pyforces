"""
Solution for LC#133: Clone Graph

https://leetcode.com/problems/clone-graph/
"""
from typing import Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def dfs(v):
            visited[v.val] = True

            if v.val not in nodes:
                new_v = Node(v.val)
                nodes[v.val] = new_v

            for adj_v in v.neighbors:
                if not visited[adj_v.val]:
                    dfs(adj_v)

                adj_ref = nodes[adj_v.val]
                new_v.neighbors.append(adj_ref)

        if node is None:
            return None

        visited = [False] * 101  # 101 nodes
        nodes: Dict[int, "Node"] = dict()
        dfs(node)

        return nodes[node.val]
