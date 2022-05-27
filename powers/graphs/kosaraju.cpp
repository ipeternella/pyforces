/*
 * Kosaraju's algorithm.
 */
#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>>& G, vector<bool>& visited, vector<int>& order, int v) {
    visited[v] = true;

    for (auto u : G[v]) {
        if (!visited[u])
            dfs(G, visited, order, u);
    }

    order.push_back(v);
}

void dfs_scc(vector<vector<int>>& GR, vector<bool>& visited, int v, vector<int>& sccs, int scc) {
    visited[v] = true;
    sccs[v] = scc;

    for (auto u : GR[v]) {
        if (!visited[u])
            dfs_scc(GR, visited, u, sccs, scc);  // all nodes of current SCC get same scc number
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
    vector<vector<int>> GR(V + 1);
    vector<int> sccs(V + 1);
    vector<bool> visited(V + 1, false);
    vector<int> topo_order;

    for (int i = 1; i <= E; i++) {
        int v, u;

        cin >> v >> u;
        G[v].push_back(u);
        GR[u].push_back(v);
    }

    // first dfs: build topological order
    for (int v = 1; v <= V; v++) {
        if (!visited[v])
            dfs(G, visited, topo_order, v);
    }

    reverse(topo_order.begin(), topo_order.end());
    fill(visited.begin(), visited.end(), false);

    int scc = 1;
    for (auto v : topo_order) {
        // traverse nodes in topo order -> traverse source nodes of G
        // source nodes of G -> SINK nodes of GR (reverse), so traverse GR to peel each SCC!
        if (!visited[v])
            dfs_scc(GR, visited, v, sccs, scc++);
    }

    for (int v = 1; v <= V; v++) {
        cout << v << " " << sccs[v] << endl;
    }

    cout << "SCCs: " << scc - 1 << endl;

    return 0;
}
