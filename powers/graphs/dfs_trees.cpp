/*
 * DFS trees from graphs.
 */
#include <bits/stdc++.h>
using namespace std;

const int NONE = -1;
bool has_cycle = false;

void dfs(vector<vector<int>>& G, vector<bool>& visited, int v, int p) {
    visited[v] = true;
    cout << v << endl;

    for (int u : G[v]) {
        if (!visited[u]) {
            dfs(G, visited, u, v);
        } else if (u != p) {
            // backedge -- for undirected graphs NEVER between parent and child
            // always between child and an ancestor of the parent
            cout << v << ", " << u << endl;
            has_cycle = true;  // single backedge: cycle!
        }
    }
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int V, E;
    cin >> V >> E;

    vector<vector<int>> G(V + 1);
    vector<bool> visited(V + 1);

    for (int i = 1; i < V; i++) {
        int v, u;
        cin >> v >> u;

        G[v].push_back(u);
        G[u].push_back(v);
    }

    // guarantee all vertices are covered on G
    int p = NONE;
    for (int v = 1; v < V; v++) {
        if (!visited[v]) {
            dfs(G, visited, v, p);
        }
    }

    // if a single backedge has been found: G has a cycle found by graph DFS
    if (has_cycle) {
        cout << "G has cycle!" << endl;
    }

    return 0;
}
