/*
 * Solution for LC#680: Valid Palindrome II
 *
 * https://leetcode.com/problems/valid-palindrome-ii/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool validPalindrome(string s) {
        int n = s.size();
        int l = 0, r = n - 1;
        int retry_l = -1, retry_r = -1;
        bool deleted = false;
        bool try_again = false;

        while (l < r) {
            if (s[l] != s[r]) {
                if (deleted) {
                    try_again = true;
                    break;
                }
                deleted = true;
                retry_l = l;
                retry_r = r;
                r--;  // try removing right-most mismatched char
            } else {
                l++;
                r--;
            }
        }

        // try removing the left-most mismatched char
        if (try_again) {
            l = retry_l + 1;
            r = retry_r;
            while (l < r) {
                if (s[l] != s[r]) {
                    return false;
                } else {
                    l++;
                    r--;
                }
            }
        }

        return true;
    }
};
