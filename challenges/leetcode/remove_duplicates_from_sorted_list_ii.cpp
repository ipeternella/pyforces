/*
 * Solution for LC#82: Remove Duplicates from Sorted List II
 *
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr = head;
        ListNode* last_unique;

        while (curr) {
            ListNode* next_node = curr->next;
            bool repeats = false;

            // find if current node repeats and place the next different node in next_node
            while (next_node && next_node->val == curr->val) {
                next_node = next_node->next;
                repeats = true;
            }

            if (!repeats) {
                if (!last_unique) {
                    head = curr;
                    last_unique = curr;
                } else {
                    last_unique->next = curr;
                    last_unique = curr;
                }
            } else {
                // if there's no next_node: the list is over
                if (!next_node) {
                    if (!last_unique)
                        return nullptr;  // no last unique so far: everything's removed

                    last_unique->next = nullptr;  // last unique becomes the last node of the list
                }
            }

            curr = next_node;
        }

        return head;
    }
};
