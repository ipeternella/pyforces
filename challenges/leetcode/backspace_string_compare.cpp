/*
 * Solution for LC#844: Backspace String Compare
 *
 * https://leetcode.com/problems/backspace-string-compare/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        // O(n) in time, O(1) in space solution as C++ strings are mutable
        int n = s.size();
        int m = t.size();
        int backspaced_n = erase_backspaced_chars(s);
        int backspaced_m = erase_backspaced_chars(t);

        if (backspaced_n != backspaced_m)
            return false;

        int i = 0;
        int j = 0;
        while (i < n and j < m) {
            // if char = '0' (erase mark) -> skip it! it was removed
            while (s[i] == '0' or s[i] == '#')
                i++;

            while (t[j] == '0' or t[j] == '#')
                j++;

            if (s[i] != t[j])
                return false;

            i++;
            j++;
        }

        return true;
    }

    // O(n) in time, O(1) in space
    int erase_backspaced_chars(string& s) {
        int n = s.size();
        int bs = 0;

        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '#') {
                bs++;
            } else {
                if (bs > 0) {
                    s[i] = '0';
                    bs--;
                }
            }
        }

        // final size after backspacing
        int size = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != '0' and s[i] != '#')
                size++;
        }

        return size;
    }
};
