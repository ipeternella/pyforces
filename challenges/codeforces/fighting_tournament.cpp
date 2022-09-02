/*
 * Solution for 1719/C: Fighting Tournament
 *
 * https://codeforces.com/problemset/problem/1719/C
 */
#include <bits/stdc++.h>
using namespace std;

int query(vector<int>& wins, int l, int r, int f) {
    int l2 = l, r2 = r;
    if (wins[r] < f)
        return 0;

    // binary search for lower bound
    int mid = l + (r - l) / 2;
    while (l < r) {
        mid = l + (r - l) / 2;
        if (wins[mid] >= f) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    int start = wins[l] < f ? l + 1 : l;

    // binary search for upper bound
    l = l2;
    r = r2;
    mid = l + (r - l) / 2;
    while (l < r) {
        mid = l + (r - l) / 2;
        if (wins[mid] <= f) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    int end = wins[l] <= f ? l + 1 : l;
    return end - start;  // amount of victories
}

void simulate(deque<int>& Q, vector<int>& wins, int r) {
    for (int i = 1; i <= r; i++) {
        int f1 = Q.at(0);
        int f2 = Q.at(1);
        Q.pop_front();
        Q.pop_front();
        if (f1 > f2) {
            Q.push_front(f1);
            Q.push_back(f2);
            wins[i] = f1;
        } else {
            Q.push_back(f1);
            Q.push_front(f2);
            wins[i] = f2;
        }
    }
}

void solve() {
    int n, q;
    cin >> n >> q;
    deque<int> Q;
    vector<int> a(n + 1);
    vector<int> wins(n + 1);
    int z = 0, Z = 0;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        Q.push_back(a[i]);
        if (a[i] > Z) {
            Z = a[i];
            z = i;
        }
    }

    // O(n) simulation
    simulate(Q, wins, n);

    // O(q*logn) - binary search for amount for victories
    while (q--) {
        int i, k;
        cin >> i >> k;

        if (k > n and i == z) {
            cout << query(wins, 1, n, a[i]) + k - n << endl;
        } else {
            k = min(k, n);
            cout << query(wins, 1, k, a[i]) << endl;
        }
    }
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--)
        solve();

    return 0;
}
