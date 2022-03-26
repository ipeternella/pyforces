/*
 * Solution for LC#1029: Two City Scheduling
 *
 * https://leetcode.com/problems/two-city-scheduling/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int n = costs.size();
        int total_cost = 0;
        vector<int> diffs;

        // assume all people go to city A only (so use only cost A which will be corrected later)
        for (int i = 0; i < n; i++) {
            total_cost += costs[i][0];
            diffs.push_back(costs[i][1] - costs[i][0]);
        }

        // sort to grab smallest city B costs
        sort(diffs.begin(), diffs.end());

        // transfer half of people from city A to city B
        // correction of the current cost that only uses city A
        for (int i = 0; i < n / 2; i++)
            total_cost += diffs[i];

        return total_cost;
    }
};
