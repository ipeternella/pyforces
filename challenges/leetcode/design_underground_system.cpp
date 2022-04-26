/*
 * Solution for LC#1396: Design Underground System
 *
 * https://leetcode.com/problems/design-underground-system/
 */
#include <bits/stdc++.h>
using namespace std;

class UndergroundSystem {
public:
    unordered_map<string, unordered_map<string, pair<int, int>>> stats;  // { "src": { "dest": (sum, n) } }
    unordered_map<int, pair<string, int>> users;                         // { 10: ("src", t1) }

    void checkIn(int id, string stationName, int t) {
        users[id] = make_pair(stationName, t);
    }

    void checkOut(int id, string stationName, int t) {
        auto user_log = users[id];

        string src_city = user_log.first;
        string dest_city = stationName;
        int t1 = user_log.second;
        int t2 = t;

        auto got_src = stats.find(src_city);
        if (got_src == stats.end()) {
            stats[src_city][dest_city] = make_pair(t2 - t1, 1);  // first time for this city pair
        } else {
            auto got_dest = stats[src_city].find(dest_city);

            if (got_dest == stats[src_city].end()) {
                stats[src_city][dest_city] = make_pair(t2 - t1, 1);  // first time for this city pair
            } else {
                auto val = got_dest->second;
                int prev_sum = val.first;
                int users = val.second;

                // extend sum and add extra user for next avg computations
                stats[src_city][dest_city] = make_pair(prev_sum + (t2 - t1), users + 1);
            }
        }
    }

    double getAverageTime(string startStation, string endStation) {
        pair<int, int> city_pair_data = stats[startStation][endStation];
        int total_time = city_pair_data.first;
        int users = city_pair_data.second;

        return (double)total_time / users;
    }
};
