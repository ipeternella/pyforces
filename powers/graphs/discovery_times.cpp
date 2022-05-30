/*
 * Node and lowest ancestor discovery times to find bridge edges on undirected graphs.
 */
#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> bridges;

void dfs(
    vector<vector<int>>& G, vector<bool>& visited, vector<int>& low, vector<int>& disc, int curr, int par, int time) {
    time++;
    visited[curr] = true;
    disc[curr] = time;
    low[curr] = time;

    for (int adj : G[curr]) {
        if (!visited[adj]) {
            dfs(G, visited, low, disc, adj, curr, time);
            // child may have found a new lowest ancestor and so does this parent
            // and both now may have a new lowest ancestor - must use low[adj]
            low[curr] = min(low[curr], low[adj]);

            if (disc[curr] < low[adj]) {
                // bridge edge -- current discovery time is smaller than adj's
                // lowest common ancestor discovery time: adj node has no backedges
                // to an ancestor of curr and hence this is a BRIDGE!
                bridges.push_back({adj, curr});
            }
        } else if (adj != par) {
            // backedge -- check if adj node is the new lowest ancestor
            // must use disc[adj] and NOT low[adj] as we want the lowest ancestor
            // and not a possible ancestor of an ancestor
            low[curr] = min(low[curr], disc[adj]);
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

    vector<vector<int>> G(V);
    vector<bool> visited(V);
    vector<int> low(V);   // discovery time of lowest ancestor
    vector<int> disc(V);  // discovery times
    int time = 0;

    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;

        G[u].push_back(v);
        G[v].push_back(u);
    }

    // dfs from start
    dfs(G, visited, low, disc, 0, -1, time);

    for (int v = 0; v < V; v++) {
        cout << "node: " << v << ", disc: " << disc[v] << ", low: " << low[v] << endl;
    }

    for (auto p : bridges) {
        cout << "bridge: (" << p.first << ", " << p.second << ")" << endl;
    }

    return 0;
}
