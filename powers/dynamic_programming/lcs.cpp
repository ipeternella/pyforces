/*
 * Longest Common Subsequence problem.
 */
#include <bits/stdc++.h>
using namespace std;

int lcs(string& s1, string& s2) {
    int m = s1.size();
    int n = s2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));

    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                continue;

            if (s1[i - 1] == s2[j - 1]) {
                // char match: use best of substrings until i - 1 AND j - 1
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
            } else {
                // char miss: pick best without one char on each substr i - 1 OR j - 1
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
            }
        }
    }

    return dp[m][n];
}

void test_should_compute_lcs_of_two_strings_1() {
    // arrange
    string s1 = "AGGTAABC";
    string s2 = "GXTXAAYBC";

    // act
    int longest = lcs(s1, s2);

    // assert
    assert(longest == 6);
}

void test_should_compute_lcs_of_two_strings_2() {
    // arrange
    string s1 = "";
    string s2 = "";

    // act
    int longest = lcs(s1, s2);

    // assert
    assert(longest == 0);
}

int main() {
    test_should_compute_lcs_of_two_strings_1();
    test_should_compute_lcs_of_two_strings_2();
}
