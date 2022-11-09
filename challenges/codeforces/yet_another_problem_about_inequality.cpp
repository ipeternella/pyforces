/*
 * Solution for 1703/F: Yet Another Problem About Pairs Satisfying an Inequality
 *
 * https://codeforces.com/problemset/problem/1703/F
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int query(vector<int>& a, int l, int r, int key) {
    int mid = l + (r - l) / 2;
    while (l < r) {
        mid = l + (r - l) / 2;

        if (a[mid] < key) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }

    return a[l] < key ? l + 1 : l;  // lower bound
}

void solve() {
    int n;
    cin >> n;

    vector<int> a(n + 1);
    vector<int> indexes;
    ll cnt = 0;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];

        if (a[i] < i)
            indexes.push_back(i);  // valid i from a in which a[i] < i
    }

    // lower bound to check how is a[j] bigger than previous indexes (indexes is sorted)
    int m = indexes.size();
    for (int i = 1; i < m; i++) {
        int j = indexes[i];
        cnt += (ll)query(indexes, 0, i - 1, a[j]);
    }

    cout << cnt << endl;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
        solve();

    return 0;
}
