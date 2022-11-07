/*
 * Solution for 1574/C: Slay the Dragon
 *
 * https://codeforces.com/problemset/problem/1574/C
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n;

    vector<ll> heros(n);
    ll all_power = 0;
    for (int i = 0; i < n; i++) {
        cin >> heros[i];
        all_power += heros[i];
    }

    sort(heros.begin(), heros.end());

    // O(M*logN) solution
    cin >> m;
    for (int i = 0; i < m; i++) {
        ll coins1 = 0, coins2 = 0;
        ll def = 0, atk = 0;
        cin >> def >> atk;

        int j = (lower_bound(heros.begin(), heros.end(), def) - heros.begin());
        int k = min(j, n - 1);

        if (heros[k] < def)
            coins1 += abs(heros[k] - def);

        ll remaining_power = all_power - heros[k];
        if (remaining_power < atk)
            coins1 += abs(remaining_power - atk);

        k = max(0, k - 1);
        if (heros[k] < def)
            coins2 += abs(heros[k] - def);

        remaining_power = all_power - heros[k];
        if (remaining_power < atk)
            coins2 += abs(remaining_power - atk);

        cout << min(coins1, coins2) << endl;
    }

    return 0;
}
