/*
 * Solution for 888/D: Almost Identity Permutations
 *
 * https://codeforces.com/contest/888/problem/D
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll choose(ll n, ll k) {
    if (k == 0)
        return 1;
    ll top = n;
    ll bottom = 1;
    for (int i = 1; i <= k - 1; i++) {
        top *= (n - i);
        bottom *= i;
    }
    bottom *= k;
    return top / bottom;
}

ll derangement(ll m, vector<ll>& dp) {
    if (dp[m] != -1)
        return dp[m];

    vector<ll> perm(m + 1);
    for (int i = 1; i <= m; i++)
        perm[i] = i;

    ll total = 0;
    do {
        ll no_match = 0;
        for (int i = 1; i <= m; i++)
            if (perm[i] != i)
                no_match++;
        if (no_match == m)
            total++;
    } while (next_permutation(perm.begin() + 1, perm.end()));

    return dp[m] = total;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int n, k;
    cin >> n >> k;
    vector<ll> dp(6, -1);  // derangement from 0 .. 5 = 6 slots required

    ll count = 0;
    for (int m = 0; m <= k; m++)
        count += choose(n, m) * derangement(m, dp);

    cout << count << endl;
    return 0;
}
