"""
Solution for LC#797: All Paths From Source to Target

https://leetcode.com/problems/all-paths-from-source-to-target/
"""
from collections import deque
from typing import Deque
from typing import List
from typing import Tuple


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q: Deque[Tuple[int, List[int]]] = deque()
        solutions: List[List[int]] = []
        path: List[int]

        q.append((0, [0]))  # path starts with node 0
        while q:
            i, path = q.popleft()
            adj = graph[i]

            for j in adj:
                path.append(j)
                updated_path = path.copy()
                q.append((j, updated_path))  # appends updated path for next iteration
                path.pop()  # pops new updated path to try other adjacent nodes

                if j == n - 1:
                    solutions.append(updated_path)  # final final destination

        return solutions
