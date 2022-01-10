"""
Solution for LC#146: LRU Cache

https://leetcode.com/problems/lru-cache/
"""
from dataclasses import dataclass
from typing import Dict
from typing import Optional


@dataclass
class Node:
    key: int
    value: int
    nxt: Optional["Node"] = None
    prev: Optional["Node"] = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def remove(self, node):
        if node == self.head:
            self.head = node.nxt
        if node == self.tail:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.nxt = node.nxt
        if node.nxt is not None:
            node.nxt.prev = node.prev

        node.nxt = None
        node.prev = None
        self.size -= 1

    def append(self, node):
        if self.size >= 1:
            self.tail.nxt = node
            node.prev = self.tail
            self.tail = node
        else:
            self.tail = node
            self.head = node

        self.size += 1


class LRUCache:
    capacity: int
    size: int
    mapping: Dict[int, Node]
    storage: DoublyLinkedList

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.mapping = dict()
        self.storage = DoublyLinkedList()

    def _make_recently_used(self, key: int, value: Optional[int] = None):
        node = self.mapping[key]
        value = node.value if value is None else value
        node.value = value

        self.storage.remove(node)
        self.storage.append(node)

    def get(self, key: int) -> int:
        if key in self.mapping:
            self._make_recently_used(key)
            return self.mapping[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self._make_recently_used(key, value)
            return

        if self.size >= self.capacity:
            node = self.mapping[self.storage.head.key]
            self.storage.remove(node)
            self.mapping.pop(node.key)
            self.size -= 1

        self.mapping[key] = Node(key, value)
        self.storage.append(self.mapping[key])
        self.size += 1
