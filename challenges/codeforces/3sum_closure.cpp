/*
 * Solution for 1698/C: 3SUM Closure
 *
 * https://codeforces.com/problemset/problem/1698/C
 */
#include <bits/stdc++.h>
using namespace std;

bool exists(vector<int>& a, int key) {
    int n = a.size();
    for (int i = 0; i < n; i++) {
        if (a[i] == key)
            return true;
    }
    return false;
}

bool solve() {
    int n;
    cin >> n;
    vector<int> a;
    int positives = 0;
    int negatives = 0;
    int zeros = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        if (x > 0) {
            positives++;
        } else if (x < 0) {
            negatives++;
        } else {
            zeros++;
        }

        if (x != 0)
            a.push_back(x);

        if (x == 0 and zeros <= 2)
            a.push_back(x);
    }

    if (positives > 2 or negatives > 2)
        return false;

    // brute force remaining triplets (m = 6 tops) with linear search
    int m = a.size();
    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            for (int k = j + 1; k < m; k++) {
                int three_sum = a[i] + a[j] + a[k];
                if (!exists(a, three_sum))
                    return false;
            }
        }
    }

    return true;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--)
        cout << (solve() ? "YES" : "NO") << endl;

    return 0;
}
