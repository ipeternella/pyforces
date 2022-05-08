/*
 * Solution for LC#1209: Remove All Adjacent Duplicates in String II
 *
 * https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string removeDuplicates(string s, int k) {
        int n = s.size();
        stack<pair<char, int>> stk;

        for (int i = 0; i < n; i++) {
            char ch = s[i];

            if (!stk.empty()) {
                char stk_ch = stk.top().first;
                int stk_ch_f = stk.top().second;

                if (stk_ch == ch) {
                    stk.push({ch, stk_ch_f + 1});
                } else {
                    stk.push({ch, 1});
                }

                // if freq on stk == k, pop all k-adjacent chars
                if (stk.top().second == k) {
                    int j = k;
                    while (j--) {
                        stk.pop();
                    }
                }
            } else {
                stk.push({ch, 1});
            }
        }

        string ans;
        while (!stk.empty()) {
            ans.push_back(stk.top().first);
            stk.pop();
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
