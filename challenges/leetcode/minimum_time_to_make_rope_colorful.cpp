/*
 * Solution for LC#1578: Minimum Time to Make Rope Colorful
 *
 * https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(string colors, vector<int>& times) {
        int m = colors.size();
        int l = 0;
        int time = 0;
        char nxt = '0';

        // greedy approach applies here, so no dp needed: O(n)
        while (l < m - 1) {
            char curr = colors[l];
            if (curr == colors[l + 1]) {
                int r = l + 1;
                while (r < m and colors[r] == curr)
                    r++;
                if (--r > l) {
                    time += remove(times, l, r);
                    l = r + 1;
                }
            } else {
                l++;
            }
        }

        return time;
    }

    int remove(vector<int>& times, int l, int r) {
        int slowest = 0;
        int acc_time = 0;
        for (int i = l; i <= r; i++) {
            acc_time += times[i];
            slowest = max(slowest, times[i]);
        }
        return acc_time - slowest;
    }
};
