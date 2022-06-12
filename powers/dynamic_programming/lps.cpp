/*
 * Longest palindromic subsequence studies.
 */
#include <bits/stdc++.h>

#include <vector>
using namespace std;

int lps(string& s, vector<vector<int>>& dp, int l, int r) {
    if (l >= r)
        return 1;

    if (r == l + 1 and s[l] == s[r])
        return 2;

    if (dp[l][r] != -1) {
        return dp[l][r];
    }

    if (s[l] == s[r]) {
        dp[l][r] = lps(s, dp, l + 1, r - 1) + 2;
        return dp[l][r];
    }

    dp[l][r] = max(lps(s, dp, l, r - 1), lps(s, dp, l + 1, r));
    return dp[l][r];
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    string s;
    int n;

    cin >> s;
    n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, -1));

    cout << "LPS" << endl;
    cout << lps(s, dp, 0, n - 1);

    return 0;
}
