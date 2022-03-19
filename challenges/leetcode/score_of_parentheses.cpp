/*
 * Solution for LC#856: Score of Parentheses
 *
 * https://leetcode.com/problems/score-of-parentheses/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int scoreOfParentheses(string s) {
        int n = s.size();
        stack<tuple<int, int, int>> stk_points;  // stk with points, left, right range
        stack<int> stk;                          // stks of the indexes of the pairs

        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                stk.push(i);
                continue;
            }

            // fetch [left, right] range covered by the parentheses
            int right = i;
            int left = stk.top();
            stk.pop();

            if (right - left == 1) {
                stk_points.push(make_tuple(1, left, right));  // simple () case
            } else {
                int updated_points = 0;
                int m = stk_points.size();

                for (int j = 0; j < m; j++) {
                    auto t = stk_points.top();
                    int points = get<0>(t);
                    int left_prev = get<1>(t);
                    int right_prev = get<2>(t);

                    // if the range is covered by a bigger range: double the points
                    if (left_prev >= left and right_prev <= right) {
                        stk_points.pop();
                        updated_points += 2 * points;
                    }
                }

                // merge the final points
                stk_points.push(make_tuple(updated_points, left, right));
            }
        }

        // final sum of the points: sum scores of all parentheses
        int points = 0;

        while (!stk_points.empty()) {
            auto t = stk_points.top();
            stk_points.pop();
            points += get<0>(t);
        }

        return points;
    }
};
