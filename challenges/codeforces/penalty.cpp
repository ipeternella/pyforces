/*
 * Solution for 1553/C: Penalty
 *
 * https://codeforces.com/problemset/problem/1553/C
 */
#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;

pii qry(string& pred, int round, bool odd_team) {
    pii score = {0, 0};
    for (int i = 1; i <= round; i++) {
        if (odd_team and (i & 1)) {
            if (pred[i] == '1')
                score.first++;
            else if (pred[i] == '?')
                score.second++;
        } else if (!odd_team and !(i & 1)) {
            if (pred[i] == '1')
                score.first++;
            else if (pred[i] == '?')
                score.second++;
        }
    }

    return score;
}

int chances(int start, bool odd_team) {
    int chances = 0;
    for (int i = start; i <= 10; i++) {
        if (odd_team and (i & 1)) {
            chances++;
        } else if (!odd_team and !(i & 1)) {
            chances++;
        }
    }
    return chances;
}

int solve() {
    string pred;
    cin >> pred;
    pred = '\0' + pred;

    int min_round = 10;
    for (int round = 1; round <= 10; round++) {
        pii score_a = qry(pred, round, true);
        pii score_b = qry(pred, round, false);

        int max_a = score_a.first + score_a.second;
        int min_b = score_b.first;
        int chances_b = chances(round + 1, false);

        if (max_a - min_b > chances_b)
            min_round = min(min_round, round);

        int max_b = score_b.first + score_b.second;
        int min_a = score_a.first;
        int chances_a = chances(round + 1, true);

        if (max_b - min_a > chances_a)
            min_round = min(min_round, round);
    }

    return min_round;
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
