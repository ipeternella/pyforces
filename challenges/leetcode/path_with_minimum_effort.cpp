/*
 * Solution for LC#1631: Path With Minimum Effort
 *
 * https://leetcode.com/problems/path-with-minimum-effort/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> efforts(m, vector<int>(n, INT_MAX));
        priority_queue<pair<int, pair<int, int>>> pq;

        // init dijkstra's
        efforts[0][0] = 0;
        pq.push({efforts[0][0], {0, 0}});

        while (!pq.empty()) {
            int prev_effort = -pq.top().first;  // negative to use pq as a min. priority queue
            auto node = pq.top().second;
            auto adj_nodes = get_adj_nodes(node, m, n);
            pq.pop();

            for (auto adj_node : adj_nodes) {
                int node_height = heights[node.first][node.second];
                int adj_node_height = heights[adj_node.first][adj_node.second];

                // new effort cannot forget previous efforts that might be bigger than curr height diff
                int new_effort = max(prev_effort, abs(node_height - adj_node_height));

                // minimum effort has been found for adj node
                if (new_effort < efforts[adj_node.first][adj_node.second]) {
                    efforts[adj_node.first][adj_node.second] = new_effort;
                    pq.push({-new_effort, {adj_node.first, adj_node.second}});  // negative for min. priority queue
                }
            }
        }

        return efforts[m - 1][n - 1];
    }

    vector<pair<int, int>> get_adj_nodes(pair<int, int> node, int m, int n) {
        vector<pair<int, int>> adj;
        int i = node.first;
        int j = node.second;

        if (i - 1 >= 0)
            adj.push_back({i - 1, j});

        if (i + 1 < m)
            adj.push_back({i + 1, j});

        if (j - 1 >= 0)
            adj.push_back({i, j - 1});

        if (j + 1 < n)
            adj.push_back({i, j + 1});

        return adj;
    }
}
