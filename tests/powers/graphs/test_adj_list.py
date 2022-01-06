import unittest
from unittest import mock

from powers.graphs.adj_list import Graph
from powers.graphs.adj_list import HashGraph


class GraphAdjListTests(unittest.TestCase):
    def test_should_create_graph(self):
        # arrange
        g = Graph(6)

        # act
        g.add_edge(0, 1)
        g.add_edge(0, 4)
        g.add_edge(2, 1)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(2, 3)
        g.add_edge(3, 5)

        # assert
        expected_adj_vertices = [[1, 4], [0, 2], [1, 3], [4, 2, 5], [0, 3, 5], [4, 3]]
        adj_vertices = list(g)  # invokes the whole generator from the Graph classs

        self.assertEqual(adj_vertices, expected_adj_vertices)

    def test_should_create_undirected_hashgraph(self):
        # arrange
        cities = ["Sao Paulo", "London", "Paris", "New York"]
        g = HashGraph(cities, directed=False)

        # act - add flights
        g.add_edge("Sao Paulo", "London")
        g.add_edge("New York", "London")
        g.add_edge("Sao Paulo", "Paris")
        g.add_edge("Paris", "New York")

        # assert
        expected_adj_vertices = [
            ("Sao Paulo", ["London", "Paris"]),
            ("New York", ["London", "Paris"]),
            ("London", ["Sao Paulo", "New York"]),
            ("Paris", ["Sao Paulo", "New York"]),
        ]
        adj_vertices = list(g)  # ["name1", ["name2", "name3", ...]]

        self.assertCountEqual(adj_vertices, expected_adj_vertices)

    def test_should_create_directed_hashgraph(self):
        # arrange
        cities = ["Sao Paulo", "London", "Paris", "New York"]
        g = HashGraph(cities, directed=True)

        # act - add flights
        g.add_edge("Sao Paulo", "London")
        g.add_edge("New York", "London")
        g.add_edge("Sao Paulo", "Paris")
        g.add_edge("Paris", "New York")

        # assert
        expected_adj_vertices = [
            ("Sao Paulo", ["London", "Paris"]),
            ("New York", ["London"]),
            ("London", []),
            ("Paris", ["New York"]),
        ]
        adj_vertices = list(g)  # ["name1", ["name2", "name3", ...]]

        self.assertCountEqual(adj_vertices, expected_adj_vertices)

    @mock.patch("builtins.print")
    def test_should_bfs_graph_for_shortest_path(self, mock_print: mock.MagicMock):
        r"""
        Graph:

               2 - 3 - - 5
             /     |   /  \
            1      |  /    6
             \     | /
               0 - 4

        One possible shortest path: [1, 0, 4, 5, 6], dist = 4
        """
        # arrange
        g = Graph(7)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(3, 5)
        g.add_edge(5, 6)
        g.add_edge(4, 5)
        g.add_edge(0, 4)
        g.add_edge(3, 4)
        g.add_edge(3, 2)

        # act
        dist, shortest_path = g.bfs(source=1, dest=6)

        # assert
        expected_shortest_path = [1, 0, 4, 5, 6]
        expected_dist = 4

        self.assertEqual(shortest_path, expected_shortest_path)
        self.assertEqual(dist, expected_dist)

    @mock.patch("builtins.print")
    def test_should_bfs_graph(self, mock_print: mock.MagicMock):
        # arrange
        g = Graph(7)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(3, 5)
        g.add_edge(5, 6)
        g.add_edge(4, 5)
        g.add_edge(0, 4)
        g.add_edge(3, 4)
        g.add_edge(3, 2)

        # act
        g.bfs(1)

        # assert
        expected_traversed_vertices = [
            mock.call(1),
            mock.call(0),
            mock.call(2),
            mock.call(4),
            mock.call(3),
            mock.call(5),
            mock.call(6),
        ]
        mock_print.assert_has_calls(expected_traversed_vertices)

    @mock.patch("builtins.print")
    def test_should_dfs_graph(self, mock_print: mock.MagicMock):
        # arrange
        g = Graph(7)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 5)
        g.add_edge(5, 6)
        g.add_edge(4, 5)
        g.add_edge(0, 4)
        g.add_edge(3, 4)

        # act
        g.dfs(1)

        # assert
        expected_traversed_vertices = [
            mock.call(1),
            mock.call(0),
            mock.call(4),
            mock.call(5),
            mock.call(3),
            mock.call(2),
            mock.call(6),
        ]
        mock_print.assert_has_calls(expected_traversed_vertices)
