#include <bits/stdc++.h>
using namespace std;

class Graph {
    int V;
    list<pair<int, int>>* adj_nodes;  // pointer to a list of adj nodes

public:
    Graph(int v) {
        V = v;
        adj_nodes = new list<pair<int, int>>[V];  // dynamic allocation of an array of V adj lists
    }

    void add_edge(int v, int u, int wt, bool directed = true) {
        adj_nodes[v].push_back({wt, u});

        if (!directed)
            adj_nodes[u].push_back({wt, v});
    }

    int dijkstra(int src, int dest) {
        vector<int> dist(V, INT_MAX);  // init dists = INF
        set<pair<int, int>> pq;  // sets, usually, are RBTs so they have an order: can be used like a priority queue

        // initialization from src node with 0 dist
        dist[src] = 0;
        pq.insert({0, src});

        while (!pq.empty()) {
            auto closer = pq.begin();  // set = RBT, so smallest weight (pair<int, int>) is returned
            int node_dist = closer->first;
            int node = closer->second;
            pq.erase(closer);

            // traverse adj nodes: each adj_node = pair<int, int>
            for (auto adj_pair : adj_nodes[node]) {
                int edge_dist = adj_pair.first;
                int adj_node = adj_pair.second;

                // if current node's distance + edge dist yields a shorter path to adj_node: update it!
                if (node_dist + edge_dist < dist[adj_node]) {
                    int smaller_dist = node_dist + edge_dist;

                    // remove previous bigger node distance and add the update dist
                    pq.erase({dist[adj_node], adj_node});
                    pq.insert({smaller_dist, adj_node});
                    dist[adj_node] = smaller_dist;
                }
            }
        }

        for (int i = 0; i < V; i++)
            cout << "Node: " << i << " Dist: " << dist[i] << endl;

        return dist[dest];
    }
};

int main() {
    Graph g(5);

    g.add_edge(0, 1, 1);
    g.add_edge(1, 2, 1);
    g.add_edge(0, 2, 4);
    g.add_edge(0, 3, 7);
    g.add_edge(2, 3, 2);
    g.add_edge(3, 4, 3);

    cout << g.dijkstra(0, 4) << endl;
}
