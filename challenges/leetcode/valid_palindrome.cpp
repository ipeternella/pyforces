/*
 * Solution for LC#125: Valid Palindrome
 *
 * https://leetcode.com/problems/valid-palindrome/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string prepare(string s) {
        string p;

        // only lower-cased valid alphanumeric chars
        for (int i = 0; i < s.size(); i++) {
            if (isalnum(s[i]))
                p.push_back(tolower(s[i]));
        }

        return p;
    }

    bool isPalindrome(string s) {
        string p = prepare(s);
        int l = 0;
        int r = p.size() - 1;

        while (l < r) {
            if (p[l] != p[r])
                return false;

            l++;
            r--;
        }

        return true;
    }
};
