/*
 * Solution for LC#581: Shortest Unsorted Continuous Subarray
 *
 * https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        stack<int> stk;
        int start = n;
        int end = 0;

        for (int i = 0; i < n; i++) {
            int num = nums[i];

            // if last numbers on stk are bigger than num, go left (pop from stk) until correct position is found
            while (!stk.empty() and nums[stk.top()] > num) {
                start = min(start, stk.top());
                stk.pop();
            }

            stk.push(i);
        }

        stk = {};
        for (int i = n - 1; i >= 0; i--) {
            int num = nums[i];

            // if last numbers on stk are smaller than num, go right (pop from stk) until correct position is found
            while (!stk.empty() and nums[stk.top()] < num) {
                end = max(end, stk.top());
                stk.pop();
            }

            stk.push(i);
        }

        return start - end == n ? 0 : end - start + 1;
    }
};
