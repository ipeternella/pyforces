/*
 * Solution for LC#1642: Furthest Building You Can Reach
 *
 * https://leetcode.com/problems/furthest-building-you-can-reach/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        priority_queue<int, vector<int>, greater<int>> min_pq;

        for (int i = 1; i < n; i++) {
            int diff = heights[i] - heights[i - 1];  // brick diff to pay to continue

            if (diff <= 0) {
                continue;
            }

            if (min_pq.size() < ladders) {
                // diffs on the min_pq are the ones covered by ladders (isolated)
                // until no more ladders are left
                min_pq.push(diff);
            } else {
                // if there are no more ladders left: add new diff to min.pq
                // and pick new minimum diff to pay with bricks (biggest diffs remain on min.pq)
                if (!min_pq.empty()) {
                    min_pq.push(diff);
                    diff = min_pq.top();
                    min_pq.pop();
                }

                bricks -= diff;
            }

            // cannot proceed further: not enough bricks and all ladders are used
            if (bricks < 0) {
                return i - 1;
            }
        }

        return n - 1;
    }
};
