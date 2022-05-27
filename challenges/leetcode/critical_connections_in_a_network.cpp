/*
 * Solution for LC#1192: Critical Connections in a Network
 *
 * https://leetcode.com/problems/critical-connections-in-a-network/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> critical_conns;
    const int NONE = -1;

    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<int>> G(n);
        vector<int> disc(n);
        vector<int> low(n);
        vector<bool> visited(n, false);
        critical_conns.clear();

        // adj list format of undirected G
        for (auto conn : connections) {
            int v = conn[0];
            int u = conn[1];

            G[v].push_back(u);
            G[u].push_back(v);
        }

        // dfs based on discovery times to find backedges and connected components
        int t = 0;
        int p = NONE;
        for (int v = 0; v < n; v++) {
            if (!visited[v])
                dfs(G, v, p, visited, disc, low, t);
        }

        return critical_conns;
    }

    void dfs(vector<vector<int>>& G, int v, int p, vector<bool>& visited, vector<int>& disc, vector<int>& low, int t) {
        t++;
        visited[v] = true;
        disc[v] = t;
        low[v] = t;

        for (int u : G[v]) {
            if (!visited[u]) {  // tree edge
                // dfs child u first
                dfs(G, u, v, visited, disc, low, t);

                // update parent's highest ancestor if child u has a backedge that leads to a higher ancestor
                low[v] = min(low[v], low[u]);

                // if low[u] (highest ancestor discovery time) is bigger than it's parent discovery time: there
                // are NO backedges to a highest ancestor of v which means we have a critical connection
                // if low[u] < disc[v]: backedges and we have a connected comp
                if (low[u] > disc[v]) {
                    critical_conns.push_back({v, u});
                }

            } else if (u != p) {  // backedge but adj node cannot be it's own parent due to undirected graph
                // update highest ancestor of current node
                low[v] = min(low[v], disc[u]);
            }
        }
    }
};
