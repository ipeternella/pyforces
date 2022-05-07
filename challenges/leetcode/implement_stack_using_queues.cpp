/*
 * Solution for LC#225: Implement Stack using Queues
 *
 * https://leetcode.com/problems/implement-stack-using-queues/
 */
#include <bits/stdc++.h>
using namespace std;

class MyStack {
public:
    // Two queue based stack with push: O(1) and pop O(n)
    queue<int> q1;
    queue<int> q2;

    void push(int x) {
        if (q1.empty())
            q2.push(x);
        else
            q1.push(x);
    }

    int pop() {
        int pop_val;

        // drain one queue to another
        if (q1.empty()) {
            while (!q2.empty()) {
                if (q2.size() > 1)
                    q1.push(q2.front());
                else
                    pop_val = q2.front();

                q2.pop();
            }
        } else {
            while (!q1.empty()) {
                if (q1.size() > 1)
                    q2.push(q1.front());
                else
                    pop_val = q1.front();

                q1.pop();
            }
        }

        return pop_val;
    }

    int top() {
        if (q1.empty())
            return q2.back();

        return q1.back();
    }

    bool empty() {
        return q1.empty() and q2.empty();
    }
};
