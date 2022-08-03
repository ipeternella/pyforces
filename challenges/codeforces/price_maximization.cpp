/*
 * Solution for 1690/E: Price Maximization
 *
 * https://codeforces.com/problemset/problem/1690/E
 */
#include <bits/stdc++.h>
#define ll long long
using namespace std;

void maximize_cost() {
    int n, K;
    cin >> n >> K;

    ll max_cost = 0;
    vector<ll> remainders(n);
    for (int i = 0; i < n; i++) {
        ll w;
        cin >> w;
        max_cost += w / K;      // a1/K + a2/K + ... sum of all integer parts directly increase max_cost
        remainders[i] = w % K;  // [a1%K, a2%K, ...] store remainders as, in pairs, they can increase max_cost
    }

    // 2 pointers: pick pairs whose remainder sum >= K (which adds one extra integer to max_cost)
    sort(remainders.begin(), remainders.end());
    int l = 0, r = n - 1;
    while (l < r) {
        if (remainders[l] + remainders[r] >= K) {
            max_cost++;  // extra integer
            r--;
            l++;
        } else {
            l++;
        }
    }

    cout << max_cost << endl;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int t;
    cin >> t;

    while (t--)
        maximize_cost();

    return 0;
}
