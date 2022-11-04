/*
 * Solution for 1692/E: Binary Deque
 *
 * https://codeforces.com/problemset/problem/1692/E
 */
#include <bits/stdc++.h>
using namespace std;

int solve() {
    int n, target;
    cin >> n >> target;
    vector<int> nums(n);
    vector<int> costs = {0};

    int init_ones = 0;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
        if (nums[i] == 1) {
            init_ones++;
            costs.push_back(i + 1);
        }
    }

    int remove = init_ones - target;
    if (remove < 0)
        return -1;

    int j = remove;
    int cost = costs[j];
    int curr = costs[j];
    int cost_r = 1;

    // start with the cost of removing only from the left side and try to
    // reduce this cost by picking ones at the right side one by one to find the global min
    for (int i = n - 1; i >= 0; i--, cost_r++) {
        if (nums[i] == 1) {
            curr = j - 1 >= 0 ? costs[j - 1] : 0;
            cost = min(cost, curr + cost_r);
            j--;
        }
    }

    return cost;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--)
        cout << solve() << endl;

    return 0;
}
