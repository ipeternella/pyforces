/*
 * Solution for LC#138: Copy List With Random Pointer
 *
 * https://leetcode.com/problems/copy-list-with-random-pointer/
 */
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> map;
        Node* curr = head;
        Node* new_head = nullptr;
        Node* new_prev;
        Node* new_node;

        while (curr) {
            // build or retrieve a new node (retrieve as it might have been a random node)
            if (map.find(curr) == map.end()) {
                new_node = new Node(curr->val);
                map[curr] = new_node;

                if (!new_head) {
                    new_head = new_node;
                } else {
                    new_prev->next = new_node;
                }

            } else {
                new_node = map[curr];
                new_prev->next = new_node;
            }

            // fix new_node's random node pointer
            if (curr->random) {
                if (map.find(curr->random) == map.end()) {
                    Node* new_random_node = new Node(curr->random->val);
                    map[curr->random] = new_random_node;
                    new_node->random = new_random_node;
                } else {
                    new_node->random = map[curr->random];
                }
            }

            curr = curr->next;
            new_prev = new_node;
        }

        return new_head;
    }
};
