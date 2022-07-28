/*
 * Solution for 1697/C: awoo's Favorite Problem
 *
 * https://codeforces.com/problemset/problem/1697/C
 */
#include <bits/stdc++.h>
using namespace std;

bool swapped(string& s, string& t, int j, char target, char condition) {
    int k = j + 1;
    while (s[k] != target) {
        if (s[k] != condition)
            return false;
        k++;
    }

    swap(s[j], s[k]);
    return true;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int q;
    cin >> q;

    while (q--) {
        int n;
        string s, t;
        cin >> n >> s >> t;

        bool possible = true;
        int j = 0;
        for (int i = 0; i < n and possible; i++) {
            if (t[i] != s[j]) {
                if (t[i] == 'c' and s[j] == 'b') {
                    // when seeking 'c' only 'b' in s can be swapped
                    possible = swapped(s, t, j, 'c', 'b');
                } else if (t[i] == 'b' and s[j] == 'a') {
                    // when seeking 'b' only 'a' in s can be swapped
                    possible = swapped(s, t, j, 'b', 'a');
                } else {
                    possible = false;
                }
            }

            j++;
        }

        cout << (possible ? "YES" : "NO") << endl;
    }

    return 0;
}
