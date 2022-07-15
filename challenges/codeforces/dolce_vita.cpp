/*
 * Solution for 1671C: Dolce Vita
 *
 * https://codeforces.com/problemset/problem/1671/C
 */
#include <bits/stdc++.h>
#define int long long int
using namespace std;

const int MAX_DAYS = 1e9 + 7;

int binary_search_day(int sums, int i, int budget, int l, int r) {
    int future_price;
    int days;

    while (l < r) {
        days = l + (r - l) / 2;
        future_price = sums + (i + 1) * days;  // correct aggregated prices

        if (future_price == budget) {
            return days;
        } else if (future_price < budget) {
            l = days + 1;
        } else {
            r = days;
        }
    }

    // check if we skipped ans due to days + 1
    future_price = sums + (i + 1) * l;
    return future_price > budget ? l - 1 : l;
}

int buy(vector<int>& costs, int budget) {
    int n = costs.size();
    int curr_day = 0, last_day = 0, prev_day = -1;
    int packs = 0;
    vector<int> sums(n);

    // prefix sum of all costs
    sort(costs.begin(), costs.end());
    sums[0] = costs[0];

    for (int i = 1; i < n; i++)
        sums[i] = sums[i - 1] + costs[i];

    // O(nlogn) - binary search last_day in which we can still buy packs
    for (int i = n - 1; i >= 0; i--) {
        last_day = binary_search_day(sums[i], i, budget, curr_day, MAX_DAYS);
        if (last_day == -1)
            continue;

        curr_day = last_day + 1;
        packs += (last_day - prev_day) * (i + 1);
        prev_day = last_day;
    }

    return packs;
}

int32_t main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t, n, b;
    cin >> t;

    while (t--) {
        cin >> n >> b;
        vector<int> costs(n);
        for (int i = 0; i < n; i++)
            cin >> costs[i];

        cout << buy(costs, b) << endl;
    }

    return 0;
}
