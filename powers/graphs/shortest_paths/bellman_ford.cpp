/*
 * Bellman-Ford's for single source shortest path (SSSP) problems. Useful as Dijkstra's algorithm
 * does not handle negative weights.
 */
#include <bits/stdc++.h>
using namespace std;

vector<int> bellman_ford(int src, int v, vector<vector<int>> edges) {
    vector<int> dist(v, INT_MAX);
    dist[src] = 0;

    // run V - 1 relaxations (longest possible path on a graph with V vertices == V - 1)
    for (int i = 0; i < v - 1; i++) {
        for (auto edge : edges) {
            int u = edge[0], v = edge[1], wt = edge[2];

            // avoid overflows with first condition if there are negative cycles
            if (dist[u] != INT_MAX && dist[u] + wt < dist[v])
                dist[v] = dist[u] + wt;
        }
    }

    // negative weight check: one iteration past (V - 1) relaxations: if any of the distances
    // do change then there's an infinite cycle as distances will keep reducing forever
    for (auto edge : edges) {
        int u = edge[0], v = edge[1], wt = edge[2];

        if (dist[u] != INT_MAX && dist[u] + wt < dist[v]) {
            dist.clear();
            return dist;  // empty dist vector
        }
    }

    return dist;
}

int main() {
    int V, E;
    cin >> V >> E;

    vector<vector<int>> edges;
    for (int i = 0; i < E; i++) {
        int u, v, wt;
        cin >> u >> v >> wt;

        edges.push_back({u, v, wt});
    }

    vector<int> dists = bellman_ford(0, V, edges);
    if (dists.size() == 0) {
        cout << "Negative weight cycle has been found!" << endl;
        exit(0);
    }

    for (int i = 0; i < V; i++)
        cout << "Node: " << i << " Dist: " << dists[i] << endl;

    return 0;
}
