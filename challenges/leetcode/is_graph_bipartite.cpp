/*
 * Solution For LC#785: Is Graph Bipartite?
 *
 * https://leetcode.com/problems/is-graph-bipartite/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();  // 0 .. n - 1
        vector<bool> visited(n, false);
        vector<char> nodes_sets(n, '-');
        queue<int> q;

        // traverse all nodes as graph may be disconnected
        for (int node = 0; node < n; node++) {
            if (visited[node])
                continue;

            // bfs
            visited[node] = true;
            nodes_sets[node] = 'a';
            q.push(node);

            while (!q.empty()) {
                int curr_node = q.front();
                vector<int> adj_nodes = graph[curr_node];

                char curr_set = nodes_sets[curr_node];
                char other_set = curr_set == 'a' ? 'b' : 'a';

                visited[curr_node] = true;
                q.pop();

                for (int adj_node : adj_nodes) {
                    char adj_node_set = nodes_sets[adj_node];

                    if (adj_node_set == '-')
                        nodes_sets[adj_node] = other_set;
                    else if (adj_node_set == curr_set)
                        return false;  // same set has been found: can't be bipartite

                    if (!visited[adj_node])
                        q.push(adj_node);
                }
            }
        }

        return true;
    }
};
