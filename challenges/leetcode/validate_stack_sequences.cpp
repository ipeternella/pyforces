/*
 * Solution for LC#946: Validate Stack Sequences
 *
 * https://leetcode.com/problems/validate-stack-sequences/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> stk;
        int n = pushed.size();
        int j = 0;  // pointer to pushed

        for (int i = 0; i < n; i++) {
            int num = popped[i];

            if (stk.empty() or stk.top() != num) {
                // no more numbers to look at: order is invalid
                if (j > n - 1)
                    return false;

                // look for num on pushed advancing j
                while (j <= n - 1 and pushed[j] != num) {
                    stk.push(pushed[j]);
                    j++;
                }

                stk.push(pushed[j]);  // found number -> move pointer ahead
                j++;
            }

            stk.pop();
        }

        return true;
    }
};
