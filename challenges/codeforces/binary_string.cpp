/*
 * Solution for 1680/C: Binary String
 *
 * https://codeforces.com/problemset/problem/1680/C
 */
#include <bits/stdc++.h>
using namespace std;

int query(vector<int>& suffix_ones, int prefix_zeros, int prefix_ones, int total_zeros) {
    int l = 0;
    int r = total_zeros - prefix_zeros;  // remaining zeros
    int zeros_removed = l + (r - l) / 2;
    while (l <= r) {
        zeros_removed = l + (r - l) / 2;
        int ones_removed = suffix_ones[zeros_removed] + prefix_ones;
        int zeros_remaining = total_zeros - zeros_removed - prefix_zeros;

        if (zeros_remaining == ones_removed) {
            break;
        } else if (zeros_remaining > ones_removed) {
            l = zeros_removed + 1;
        } else {
            r = zeros_removed - 1;
        }
    }
    return zeros_removed;
}

void removal_min_cost() {
    string s;
    cin >> s;

    int n = s.size();
    vector<int> suffix(n + 1);
    int total_zeros = count(s.begin(), s.end(), '0');
    int min_cost = total_zeros;

    // suffix vector with suffix[zeros_removed] = ones_removed (quick way to compute costs)
    int j = 1, count = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '1') {
            count++;
        } else {
            suffix[j] += suffix[j - 1] + count;
            count = 0;
            j++;
        }
    }

    // binary search amount of zeros to be removed: O(nlogn) solution
    int prefix_zeros = 0;
    int prefix_ones = 0;
    for (int i = -1; i < n; i++) {
        if (i >= 0 and s[i] == '0')
            prefix_zeros++;
        if (i >= 0 and s[i] == '1')
            prefix_ones++;

        // binary search amount of zeros removed on the suffix
        int suffix_zeros = query(suffix, prefix_zeros, prefix_ones, total_zeros);
        int zeros_remaining = total_zeros - suffix_zeros - prefix_zeros;
        int ones_removed = suffix[suffix_zeros] + prefix_ones;
        min_cost = min(min_cost, max(zeros_remaining, ones_removed));
    }

    cout << min_cost << endl;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--)
        removal_min_cost();

    return 0;
}
