/*
 * Disjoint Set Union implementation on a graph with optimizations like path compression
 * and union by rank.
 */
#include <bits/stdc++.h>
using namespace std;

class Graph {
    int V;
    vector<pair<int, int>> edges;  // list of edges instead of adj lists
    vector<int> parent;
    vector<int> rank;

public:
    Graph(int _V) {
        V = _V;
        parent = vector<int>(V, -1);
        rank = vector<int>(V, 1);  // rank starts as 1
    }

    void add_edge(int u, int v) {
        edges.push_back({u, v});
    }

    int find_set(int i, vector<int>& parent) {
        // base case: no parent -> set leader
        if (parent[i] == -1) {
            return i;
        }

        return find_set(parent[i], parent);
    }

    // optimization
    int find_set_path_compression(int i, vector<int>& parent) {
        // base case: no parent -> set leader (or super parent)
        if (parent[i] == -1) {
            return i;
        }

        // once a set leader has been found (ultimate parent), update all the paths
        // with such value: path compression
        parent[i] = find_set(parent[i], parent);
        return parent[i];
    }

    void union_set(int x, int y, vector<int>& parent) {
        int s1 = find_set(x, parent);
        int s2 = find_set(y, parent);

        // add any set as the parent of the other set
        if (s1 != s2)
            parent[s2] = s1;
    }

    // optimization - together with path compression - find/set run in O(1)
    void union_set_by_rank(int x, int y, vector<int>& parent, vector<int>& rank) {
        int s1 = find_set(x, parent);
        int s2 = find_set(y, parent);

        if (s1 != s2) {
            // union by rank -- avoids bigger trees
            if (rank[s1] < rank[s2]) {
                parent[s1] = s2;
                rank[s2] += rank[s1];
            } else {
                parent[s2] = s1;
                rank[s1] += rank[s2];
            }
        }
    }

    bool has_cycle() {
        for (auto edge : edges) {
            int i = edge.first;
            int j = edge.second;

            int s1 = find_set_path_compression(i, parent);
            int s2 = find_set_path_compression(j, parent);

            if (s1 != s2) {
                union_set_by_rank(s1, s2, parent, rank);
            } else {
                return true;
            }
        }

        return false;
    }
};

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int V, E;
    cin >> V >> E;

    Graph g(V);
    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;

        g.add_edge(u, v);
    }

    cout << "G has cycle: " << (g.has_cycle() ? "yes" : "no") << endl;
}
