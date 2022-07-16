/*
 * Solution for 1613/C: Poisoned Dagger
 *
 * https://codeforces.com/problemset/problem/1613/C
 */
#include <bits/stdc++.h>
#define int long long
using namespace std;

const int MAX_K = 1e18 + 7;

int damage(vector<int>& hits, int k) {
    int n = hits.size();
    int dmg = 0;
    for (int i = 0; i < n; i++) {
        if (i < n - 1 and hits[i] + k - 1 >= hits[i + 1]) {
            dmg += hits[i + 1] - hits[i];
        } else {
            dmg += k;
        }
    }

    return dmg;
}

int select_dagger(vector<int>& hits, int h) {
    int k_low = 1, k_high = MAX_K;
    int k;

    while (k_low < k_high) {
        k = k_low + (k_high - k_low) / 2;
        if (damage(hits, k) <= h) {
            k_low = k + 1;
        } else {
            k_high = k;
        }
    }

    if (damage(hits, k - 1) >= h) {
        return k - 1;
    } else if (damage(hits, k) >= h) {
        return k;
    } else {
        return k + 1;
    }
}

int32_t main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--) {
        int n, h;
        cin >> n >> h;

        vector<int> hits(n);
        for (int i = 0; i < n; i++)
            cin >> hits[i];

        cout << select_dagger(hits, h) << endl;
    }

    return 0;
}
