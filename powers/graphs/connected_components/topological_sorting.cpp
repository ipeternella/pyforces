/*
 * Topological sorting of DAGs.
 */
#include <bits/stdc++.h>
using namespace std;

void print_graph(vector<vector<int>> G) {
    int V = G.size();
    for (int v = 1; v < V; v++) {
        cout << v << ": ";
        for (int j = 0; j < G[v].size(); j++) {
            cout << G[v][j] << " ";
        }
        cout << endl;
    }
}

void read_graph(vector<vector<int>>& G, int E) {
    for (int i = 1; i <= E; i++) {
        int v1, v2;
        cin >> v1 >> v2;

        G[v1].push_back(v2);
    }
}

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

/*
 * Topological sorting: relies on a traditional DFS algorithm.
 */
vector<int> topological_sort(vector<vector<int>>& G) {
    int V = G.size();
    vector<bool> visited(V);
    vector<int> order;

    for (int v = 1; v < V; v++) {
        if (!visited[v]) {
            dfs(G, v, visited, order);
        }
    }

    // reverse final order to complete topological sorting
    reverse(order.begin(), order.end());
    return order;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int V, E;
    cin >> V >> E;

    // DAG in adj list format - care as we are not detecting graph cycles
    vector<vector<int>> G(V + 1);
    vector<int> topological_order;

    read_graph(G, E);
    topological_order = topological_sort(G);

    for (int v : topological_order) {
        cout << v << " ";
    }

    return 0;
}
