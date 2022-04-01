/*
 * Solution for LC#344: Reverse String
 *
 * https://leetcode.com/problems/reverse-string/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void swap(vector<char>& s, int i, int j) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }

    void reverseString(vector<char>& s) {
        int n = s.size();

        if (n == 1)
            return;

        for (int i = 0; i < n / 2; i++) {
            swap(s, i, n - 1 - i);
        }
    }
};
