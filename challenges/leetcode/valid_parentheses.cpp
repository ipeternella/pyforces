/*
 * Solution for LC#20: Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        int n = s.size();
        stack<char> stk;  // holds last open parentheses

        for (int i = 0; i < n; i++) {
            char ch = s[i];
            if (ch == '(' or ch == '{' or ch == '[') {
                stk.push(ch);
            } else {
                if (stk.empty())
                    return false;  // closing bracket needs a pair

                char last_open = stk.top();
                char required;
                switch (last_open) {
                    case '(':
                        required = ')';
                        break;
                    case '[':
                        required = ']';
                        break;
                    default:
                        required = '}';
                }

                if (required != ch)
                    return false;

                stk.pop();
            }
        }

        return stk.empty() ? true : false;
    }
};
