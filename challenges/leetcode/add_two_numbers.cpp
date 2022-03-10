/*
 * Solution for LC#2: Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/
 */
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* big_sum(ListNode* l1, ListNode* l2) {
        ListNode* head = nullptr;
        ListNode* prev = nullptr;
        ListNode* curr1 = l1;
        ListNode* curr2 = l2;
        int carry = 0;

        // l1 is the smaller number (and list)
        while (curr1) {
            int d1 = curr1->val;
            int d2 = curr2->val;
            int s = d1 + d2 + carry;
            int d_rslt = s % 10;
            carry = s / 10;

            if (!head) {
                head = new ListNode(d_rslt);
                prev = head;
            } else {
                prev->next = new ListNode(d_rslt);
                prev = prev->next;
            }

            curr1 = curr1->next;
            curr2 = curr2->next;
        }

        while (curr2) {
            int d2 = curr2->val;
            int s = d2 + carry;
            int d_rslt = s % 10;
            carry = s / 10;

            prev->next = new ListNode(d_rslt);
            prev = prev->next;
            curr2 = curr2->next;
        }

        if (carry == 1)
            prev->next = new ListNode(1);

        return head;
    }

    int size(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        int size = fast ? 2 : 1;

        while (fast) {
            slow = slow->next;
            fast = fast->next;

            if (fast) {
                size++;

                if (fast->next) {
                    size++;
                    fast = fast->next;
                } else {
                    fast = nullptr;
                }
            }
        }

        return size;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* bigger_list;
        ListNode* smaller_list;
        int n1 = size(l1);
        int n2 = size(l2);

        bigger_list = n1 > n2 ? l1 : l2;
        smaller_list = n1 > n2 ? l2 : l1;

        return big_sum(smaller_list, bigger_list);
    }
};
