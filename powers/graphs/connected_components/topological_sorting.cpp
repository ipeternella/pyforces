/*
 * Topological sorting traversal for directed graphs. The graphs should be DAGs
 * but this algorithm does not check for cycles. Used a customized dfs for that.
 */
#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>>& G, int v, vector<bool>& visited, vector<int>& order) {
    visited[v] = true;

    for (int u : G[v]) {
        if (!visited[u]) {
            dfs(G, u, visited, order);
        }
    }

    // for topological sorting: only push node after its dependencies
    order.push_back(v);
}

vector<int> topological_sort(vector<vector<int>>& G) {
    int V = G.size();
    vector<bool> visited(V);
    vector<int> order;

    for (int v = 0; v < V; v++) {
        if (!visited[v]) {
            dfs(G, v, visited, order);
        }
    }

    // reverse final order to complete topological sorting
    reverse(order.begin(), order.end());
    return order;
}

// helper functions
void print_graph(vector<vector<int>> G) {
    int V = G.size();
    for (int v = 0; v < V; v++) {
        cout << v << ": ";
        for (int j = 0; j < G[v].size(); j++) {
            cout << G[v][j] << " ";
        }
        cout << endl;
    }
}

void read_directed_graph(vector<vector<int>>& G, int E) {
    for (int i = 0; i <= E; i++) {
        int v1, v2;
        cin >> v1 >> v2;

        G[v1].push_back(v2);
    }
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int V, E;
    cin >> V >> E;

    // DAG in adj list format - care as we are not detecting graph cycles
    vector<vector<int>> G(V);
    vector<int> topological_order;
    read_directed_graph(G, E);

    topological_order = topological_sort(G);

    for (int v : topological_order) {
        cout << v << " ";
    }

    return 0;
}
