/*
 * Solution for LC#1249: Minimum Remove to Make Valid Parentheses
 *
 * https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        deque<int> stk;
        string buffer;
        string rslt;
        int n = s.size();
        int counter = 0;

        for (int i = 0; i < n; i++) {
            char ch = s[i];

            if (ch == ')') {
                // don't add a parentheses without a match!
                if (stk.empty())
                    continue;

                stk.pop_back();
            } else if (ch == '(') {
                stk.push_back(counter);
            }

            counter++;
            buffer.push_back(ch);
        }

        if (stk.empty())
            return buffer;

        // remaining open parentheses -- remove them!
        for (int i = 0; i < buffer.size(); i++) {
            int j = stk.front();

            if (i == j and !stk.empty()) {
                stk.pop_front();
            } else {
                rslt.push_back(buffer[i]);
            }
        }

        return rslt;
    }
};
