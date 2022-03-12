/*
 * Solution for LC#141: Linked List Cycle
 *
 * https://leetcode.com/problems/linked-list-cycle/
 */
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head ? head->next : nullptr;
        bool has_cycle = false;

        // breaks if the list reaches an end (fast == nullptr)
        // or if fast catches slow in a cycle (has_cycle == true)
        while (fast and !has_cycle) {
            slow = slow->next;
            fast = fast->next ? fast->next->next : nullptr;
            has_cycle = slow == fast;
        }

        return has_cycle;
    }
};
