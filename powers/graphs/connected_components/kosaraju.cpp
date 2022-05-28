/*
 * Kosaraju's algorithm for finding strongly connected components
 * on directed graphs.
 */
#include <bits/stdc++.h>
using namespace std;

void dfs_topo(vector<vector<int>>& G, vector<bool>& visited, vector<int>& order, int v) {
    visited[v] = true;

    for (auto u : G[v]) {
        if (!visited[u])
            dfs_topo(G, visited, order, u);
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

pair<int, vector<int>> kosaraju(vector<vector<int>>& G, vector<vector<int>>& GR) {
    int V = G.size();  // 0-indexed nodes
    vector<int> sccs(V);
    vector<bool> visited(V, false);
    vector<int> topo_order;

    // first dfs: build topological order
    for (int v = 0; v < V; v++) {
        if (!visited[v])
            dfs_topo(G, visited, topo_order, v);
    }
    reverse(topo_order.begin(), topo_order.end());

    // second dfs: use transposed graph based on topological order
    fill(visited.begin(), visited.end(), false);
    int total_sccs = 1;

    for (auto v : topo_order) {
        // source nodes of G -> SINK nodes of GR (reverse), so traverse GR to peel each SCC!
        if (!visited[v])
            dfs_scc(GR, visited, v, sccs, total_sccs++);
    }

    return {total_sccs - 1, sccs};
}

void read_directed_graph_with_transpose(vector<vector<int>>& G, vector<vector<int>>& GR, int E) {
    for (int i = 0; i < E; i++) {
        int v, u;

        cin >> v >> u;
        G[v].push_back(u);   // directed graph
        GR[u].push_back(v);  // transposed graph (reversed)
    }
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int V, E;
    cin >> V >> E;

    vector<vector<int>> G(V);
    vector<vector<int>> GR(V);
    read_directed_graph_with_transpose(G, GR, E);

    auto result = kosaraju(G, GR);

    int total_sccs = result.first;
    vector<int> sccs = result.second;
    for (int v = 0; v < V; v++)
        cout << v << " " << sccs[v] << endl;

    cout << "SCCs: " << total_sccs << endl;
    return 0;
}
