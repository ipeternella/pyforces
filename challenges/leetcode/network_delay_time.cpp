/*
 * Solution for LC#743: Network Delay Time
 *
 * https://leetcode.com/problems/network-delay-time/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        priority_queue<pair<int, int>> pq;
        vector<vector<pair<int, int>>> adjs = adj_lists(times, n);
        vector<int> delays(n + 1, INT_MAX);

        // dijkstra's for network delays
        delays[k] = 0;
        pq.push({0, k});

        while (!pq.empty()) {
            int s_w = -pq.top().first;  // min. priority queue
            int s = pq.top().second;
            pq.pop();

            for (auto adj : adjs[s]) {
                int u = adj.first;
                int u_w = adj.second;

                // shortest delay for network traffic
                if (s_w + u_w < delays[u]) {
                    delays[u] = s_w + u_w;
                    pq.push({-delays[u], u});
                }
            }
        }

        int t = -INT_MAX;
        for (int i = 1; i < n + 1; i++) {
            t = max(t, delays[i]);
        }

        return t == INT_MAX ? -1 : t;
    }

    // converts input into adj lists notation
    vector<vector<pair<int, int>>> adj_lists(vector<vector<int>>& times, int n) {
        vector<vector<pair<int, int>>> adjs(n + 1);
        int len = times.size();

        for (int i = 0; i < len; i++) {
            adjs[times[i][0]].push_back({times[i][1], times[i][2]});
        }

        return adjs;
    }
};
