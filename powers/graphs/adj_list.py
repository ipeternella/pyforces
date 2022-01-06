"""
Module with graphs represented with adjacency lists.
"""
from collections import deque as Queue
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Tuple


class Node:
    name: str
    adj_list: List[str]

    def __init__(self, name: str) -> None:
        self.name = name
        self.adj_list = []


class HashGraph:
    directed: bool
    vertices: Dict[str, Node]

    def __init__(self, names: List[str], directed: bool = False) -> None:
        self.vertices = dict()
        self.directed = directed
        for name in names:
            self.vertices[name] = Node(name)

    def add_edge(self, name_1: str, name_2: str) -> None:
        self.vertices[name_1].adj_list.append(name_2)

        if not self.directed:
            self.vertices[name_2].adj_list.append(name_1)

    def __iter__(self) -> Generator[Tuple[str, List[str]], None, None]:
        for node_name, node in self.vertices.items():
            yield node_name, node.adj_list


class Graph:
    v: int
    vertices: List
    directed: bool

    def __init__(self, v: int, directed: bool = False) -> None:
        self.v = v
        self.directed = directed
        self.vertices = [[] for _ in range(v)]

    def add_edge(self, v1: int, v2: int) -> None:
        self.vertices[v1].append(v2)

        if not self.directed:
            self.vertices[v2].append(v1)

    def bfs(self, source: int, dest: Optional[int] = None) -> Optional[Tuple[int, List[int]]]:  # O(V + E)
        q: Queue[int] = Queue()
        visited = [False] * self.v

        # vars for shortest paths
        parent = [-1] * self.v
        dist = [0] * self.v  # bfs for shortest path on undirected graphs only
        shortest_path = []

        q.append(source)
        while q:
            vertex = q.popleft()
            visited[vertex] = True

            # >> work each node here <<
            print(vertex)

            for adj_vertex in self.vertices[vertex]:
                if not visited[adj_vertex]:
                    q.append(adj_vertex)
                    visited[adj_vertex] = True  # [!]: important to avoid duplicates
                    parent[adj_vertex] = vertex  # useful to backtrack parents to find shortest paths
                    dist[adj_vertex] = dist[vertex] + 1

        if dest is not None:
            curr_vertex = dest

            while curr_vertex != source:
                shortest_path.append(curr_vertex)
                curr_vertex = parent[curr_vertex]  # goes back to its parent
            shortest_path.append(source)

            return dist[dest], shortest_path[::-1]

        return None

    def dfs(self, source: int) -> None:
        def dfs_aux(vertex: int, visited: List[bool]):
            visited[vertex] = True

            # >> work each node here <<
            print(vertex)

            for adj_vertex in self.vertices[vertex]:
                if not visited[adj_vertex]:
                    dfs_aux(adj_vertex, visited)

        visited = [False] * self.v
        dfs_aux(source, visited)

    def __iter__(self) -> Generator[List[int], None, None]:
        for adj_list in self.vertices:
            yield adj_list
