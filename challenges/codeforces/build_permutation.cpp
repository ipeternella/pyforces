/*
 * Solution for 1713/C: Build Permutation
 *
 * https://codeforces.com/problemset/problem/1713/C
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll next_ps(ll x) {
    ll ps = 0;
    while (ps * ps < x)
        ps++;
    return ps * ps;
}

void solve() {
    int n;
    cin >> n;
    vector<int> perm(n, -1);
    int target = n - 1;

    while (target >= 0) {
        ll ps = next_ps(target);
        int i = ps - target;
        int j = 0;

        while (i + j < n and target >= 0) {
            if (perm[i + j] != -1)
                break;

            perm[i + j] = target;
            target--;
            j++;
        }
    }

    for (int i = 0; i < n; i++)
        cout << perm[i] << " ";

    cout << endl;
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
