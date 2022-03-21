/*
 * Solution for LC#895: Maximum Frequency Stack
 *
 * https://leetcode.com/problems/maximum-frequency-stack/
 */
#include <bits/stdc++.h>
using namespace std;

class FreqStack {
    vector<stack<int>> freq_stks;  // stacks of numbers with the same frequency
    unordered_map<int, int> freqs;
    int max_freq = 0;

public:
    FreqStack() : freq_stks(20001) {}

    void push(int val) {
        auto has_key = freqs.find(val);
        int f = 0;

        if (has_key != freqs.end())
            f = has_key->second;

        // based on the freq, insert it at the appropriate stack
        freq_stks[f + 1].push(val);

        // update freq map
        freqs[val] = f + 1;

        // check if we should be pointing to a stack with more freq elements
        max_freq = max(max_freq, f + 1);
    }

    int pop() {
        int val = freq_stks[max_freq].top();
        int prev_f = freqs[val];

        // update freq map of val
        freq_stks[max_freq].pop();
        freqs[val] = prev_f - 1;

        // if the stack is empty: reduce max_freq to move to the next stk
        if (freq_stks[max_freq].empty())
            max_freq--;

        return val;
    }
};
