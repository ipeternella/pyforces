/*
 * Lowest Common Ancestor (LCA) related code.
 */
#include <bits/stdc++.h>
using namespace std;

// dfs to fetch parents and depths - runs in O(N)
void dfs(vector<vector<int>>& G, vector<int>& parents, vector<int>& depths, int v, int par) {
    int new_depth = par == -1 ? 0 : depths[par] + 1;
    parents[v] = par;
    depths[v] = new_depth;

    for (auto u : G[v]) {
        dfs(G, parents, depths, u, v);
    }
}

// runs in O(N) -- two pointers
int LCA(vector<int>& depths, vector<int>& parents, int u, int v) {
    if (u == v)
        return u;

    // avoid more ifs: u must be deeper than v
    if (depths[u] < depths[v])
        swap(u, v);

    // advancer deeper node up until there's no more diff
    int depth_diff = depths[u] - depths[v];
    while (depth_diff--) {
        u = parents[u];  // climp up to it's parent
    }

    // depths are the same -- advance both pointers together until they are the same
    while (u != v) {
        u = parents[u];
        v = parents[v];
    }

    return u;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int V, E;
    cin >> V >> E;

    vector<vector<int>> tree(V);
    vector<int> depths(V);
    vector<int> parents(V);

    // builds a tree (graph without backedges/cycles)
    // works with graphs too but requires visited (bool) array checks
    // to produce a DFS tree out of the graph
    for (int i = 0; i < E; i++) {
        int v, u;
        cin >> v >> u;

        tree[v].push_back(u);
    }

    // preprocessing: O(N) dfs to fetch parents & depths
    dfs(tree, parents, depths, 0, -1);
    for (int v = 0; v < V; v++) {
        cout << v << ", depth: " << depths[v] << endl;
    }

    // LCA -- two pointers technique
    cout << LCA(depths, parents, 8, 10) << endl;
    cout << LCA(depths, parents, 9, 8) << endl;
    cout << LCA(depths, parents, 9, 7) << endl;
    cout << LCA(depths, parents, 8, 11) << endl;

    return 0;
}
