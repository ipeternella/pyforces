/*
 * Solution for LC#456: 132 Pattern
 *
 * https://leetcode.com/problems/132-pattern/
 */
#include <bits/stdc++.h>
using namespace std;
#define NONE -INT_MAX

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        stack<int> stk;
        int last = NONE;

        for (int i = n - 1; i >= 0; i--) {
            int num = nums[i];
            if (last != NONE and last > num) {
                return true;  // if last is bigger than current num, num is '1' of '132' pattern
            }

            // drain the stack fetching the biggest that is still smaller than num
            while (!stk.empty() and num > stk.top()) {
                last = stk.top();  // last is the biggest but smaller than num ('2' of '132' pattern)
                stk.pop();
            }

            // remains on the stack: the biggest num ('3' of '132' pattern)
            stk.push(num);
        }

        return false;
    }
};
