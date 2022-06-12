/*
 * Knapsack-related problems.
 */
#include <bits/stdc++.h>
using namespace std;

#define DEBUG false

/*
 * Knapsack 01: items can be picked only once and NO repetitions are allowed. DP state
 * requires 2 variables: dp[i][w] <- value
 *
 * Time complexity: O(N * W)
 * Space complexity: O(N * W)  -- can be improved, if necessary
 */
int knapsack_01(vector<int> weights, vector<int> values, int W) {
    int n = values.size();
    vector<vector<int>> dp(n, vector<int>(W + 1));

    // init dp state
    for (int i = 0; i < n; i++)
        for (int w = 0; w <= W; w++)
            if (weights[i] <= w)
                dp[i][w] = values[i];

    for (int i = 1; i < n; i++) {
        for (int w = 0; w <= W; w++) {
            if (w - weights[i] >= 0)
                dp[i][w] = max(dp[i - 1][w - weights[i]] + values[i], dp[i - 1][w]);
        }
    }

    if (DEBUG) {
        for (int i = 0; i < n; i++) {
            for (int w = 0; w <= W; w++) {
                cout << dp[i][w] << " ";
            }
            cout << endl;
        }
    }

    return dp[n - 1][W];
}

/*
 * Knapsack 01: with top-down approach. Notice two variables are also used for the DP state as we must keep
 * track of which item we are currently trying to pick (not an unbound knapsack problem).
 */
int memo_knapsack_01(vector<int>& weights, vector<int>& values, vector<vector<int>>& dp, int W, int i) {
    if (i < 0)
        return 0;

    if (dp[i][W] != -1)
        return dp[i][W];

    if (weights[i] <= W) {
        dp[i][W] =
            max(memo_knapsack_01(weights, values, dp, W - weights[i], i - 1) + values[i],
                memo_knapsack_01(weights, values, dp, W, i - 1));

        return dp[i][W];
    }

    dp[i][W] = memo_knapsack_01(weights, values, dp, W, i - 1);
    return dp[i][W];
}

/*
 * Knapsack Fractional: items can only be picked once but they can be broken to fit into
 * the knapsack. No DP is needed as a greedy algorithm applies here.
 *
 * Time complexity: O(NlogN) -- sorting by ratio
 * Space complexity: O(N)
 */
struct Item {
    int value;
    int weight;
    double ratio;
};

double knapsack_fractional(vector<int> weights, vector<int> values, int W) {
    auto sort_by_ratio = [](Item item1, Item item2) { return item1.ratio > item2.ratio; };
    int n = values.size();
    vector<Item> items;  // easier to sort with a struct with a vi, wi and ratio
    double value = 0.0;

    for (int i = 0; i < n; i++) {
        Item item = {values[i], weights[i], (double)values[i] / weights[i]};
        items.push_back(item);
    }

    // sort by highest v/w ratio -- greedy strategy applies so no DP is needed
    sort(items.begin(), items.end(), sort_by_ratio);

    for (int i = 0; i < n; i++) {
        if (items[i].weight <= W) {
            // item fits the bag, put it as a whole
            W -= items[i].weight;
            value += items[i].value;
        } else {
            // item is heavier than remaining W -- add its fractional (wi > W)
            value += ((double)W / items[i].weight) * items[i].value;
        }
    }

    return value;
}

/*
 * Knapsack Unbound: each item can be picked indefinitely (as many times as we can fit it into
 * the knapsack). As such, there's no need for a DP with two states due to the fact that we must
 * must always look all the items. DP with a single state is enough: dp[w] <- value
 *
 * Time complexity: O(N * W)
 * Space complexity: O(W)
 */
int knapsack_unbound(vector<int> weights, vector<int> values, int W) {
    int n = values.size();
    vector<int> dp(W + 1, 0);

    for (int w = 0; w <= W; w++) {
        for (int i = 0; i < n; i++) {
            // need to check all the items all the time (they are always available)
            if (weights[i] <= w)
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);  // pick or not
        }
    }

    return dp[W];
}

/*
 * Knapsack Unbound: top-down approach. Notice the dp state with a single variable as all the
 * items can be taken repeatedly so each stack frame must create n subproblems picking each
 * item and getting the max return of each of these subproblems.
 */
int memo_knapsack_unbound(vector<int> weights, vector<int> values, vector<int>& dp, int W) {
    int n = weights.size();
    int v = 0;

    if (W == 0)
        return 0;

    if (dp[W] != -1) {
        return dp[W];
    }

    // check all items every time as it's an unbound knapsack problem
    for (int i = 0; i < n; i++)
        if (weights[i] <= W)
            v = max(v, memo_knapsack_unbound(weights, values, dp, W - weights[i]) + values[i]);

    dp[W] = v;
    return dp[W];
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int W, n;
    cin >> W >> n;

    vector<int> weights;
    vector<int> values;

    while (n--) {
        int w;
        cin >> w;
        weights.push_back(w);
    }

    n = weights.size();
    while (n--) {
        int v;
        cin >> v;
        values.push_back(v);
    }

    cout << "Knapsack 01 (DP 2 variables)" << endl;
    cout << knapsack_01(weights, values, W) << endl;

    cout << "Knapsack 01 (top-down)" << endl;
    n = weights.size();
    vector<vector<int>> dp(n, vector<int>(W + 1, -1));
    cout << memo_knapsack_01(weights, values, dp, W, n - 1) << endl;

    cout << "Knapsack Fractional (Greedy)" << endl;
    cout << knapsack_fractional(weights, values, W) << endl;

    cout << "Knapsack Unbound (DP 1 variable)" << endl;
    cout << knapsack_unbound(weights, values, W) << endl;

    cout << "Knapsack Unbound (top-down)" << endl;
    vector<int> dp2(W + 1, -1);
    cout << memo_knapsack_unbound(weights, values, dp2, W) << endl;

    return 0;
}
