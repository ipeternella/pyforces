/*
 * Solution for LC#740: Delete and Earn
 *
 * https://leetcode.com/problems/delete-and-earn/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<int> freqs(10001, 0);
        vector<int> unique_nums;

        // grab unique nums and their frequencies
        for (int i = 0; i < nums.size(); i++) {
            if (freqs[nums[i]] == 0)
                unique_nums.push_back(nums[i]);

            freqs[nums[i]]++;
        }
        sort(unique_nums.begin(), unique_nums.end());

        // dp state definition: only constant space is required (like in Fibonacci sequence)
        int points = unique_nums[0] * freqs[unique_nums[0]];
        int prev_points = points;
        int prev_prev_points = 0;

        for (int i = 1; i < unique_nums.size(); i++) {
            int curr = unique_nums[i];
            int prev = unique_nums[i - 1];

            if (curr == prev + 1) {
                // pick curr number (add to prev_prev_points) or do not pick it all!
                points = max(prev_prev_points + curr * freqs[curr], prev_points);
            } else {
                // curr number is not adjacent to previous one: always pick it up!
                points = prev_points + curr * freqs[curr];
            }

            prev_prev_points = prev_points;
            prev_points = points;
        }

        return points;
    }
};
