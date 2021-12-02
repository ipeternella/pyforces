import unittest

from powers.heap import MaxHeap
from powers.heap import MinHeap


class HeapTests(unittest.TestCase):
    def test_should_build_max_heap(self):
        # arrange
        heap = MaxHeap()

        # act
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.insert(4)

        # assert
        self.assertEqual(heap.heap, [4, 3, 2, 1])

    def test_should_build_max_heap_with_list(self):
        # arrange
        heap = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

        # assert
        self.assertEqual(heap.heap, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_should_build_min_heap(self):
        # arrange
        heap = MinHeap()

        # act
        heap.insert(3)
        heap.insert(1)
        heap.insert(4)
        heap.insert(2)

        # assert
        self.assertEqual(heap.heap, [1, 2, 4, 3])

    def test_should_build_min_heap_with_list(self):
        # arrange
        heap = MinHeap([7, 5, 3, 2])

        # assert
        self.assertEqual(heap.heap, [2, 5, 3, 7])

    def test_should_pop_items_from_min_heap(self):
        # arrange
        heap = self.build_min_heap_one()

        # act and assert
        self.assertEqual(heap.pop_min(), 1)
        self.assertEqual(heap.heap, [2, 3, 4])

        self.assertEqual(heap.pop_min(), 2)
        self.assertEqual(heap.heap, [3, 4])

        self.assertEqual(heap.pop_min(), 3)
        self.assertEqual(heap.heap, [4])

        self.assertEqual(heap.pop_min(), 4)
        self.assertEqual(heap.heap, [])

        self.assertIsNone(heap.pop_min())

    def test_should_pop_items_from_max_heap(self):
        # arrange
        heap = self.build_max_heap_one()

        # act and assert
        self.assertEqual(heap.pop_max(), 4)
        self.assertEqual(heap.heap, [3, 1, 2])

        self.assertEqual(heap.pop_max(), 3)
        self.assertEqual(heap.heap, [2, 1])

        self.assertEqual(heap.pop_max(), 2)
        self.assertEqual(heap.heap, [1])

        self.assertEqual(heap.pop_max(), 1)
        self.assertEqual(heap.heap, [])

        self.assertIsNone(heap.pop_max())

        # act - reinsert items
        heap.insert(5)
        heap.insert(1)
        heap.insert(12)
        heap.insert(30)

        # assert
        self.assertEqual(heap.heap, [30, 12, 5, 1])

        # act
        self.assertEqual(heap.pop_max(), 30)
        self.assertEqual(heap.heap, [12, 1, 5])

        self.assertEqual(heap.pop_max(), 12)
        self.assertEqual(heap.heap, [5, 1])

        # act
        heap.insert(17)

        # assert
        self.assertEqual(heap.heap, [17, 1, 5])

        heap.increase_key(2, 20)
        self.assertEqual(heap.heap, [20, 1, 17])

        heap.increase_key(1, 30)
        self.assertEqual(heap.heap, [30, 20, 17])

    def build_max_heap_one(self) -> MaxHeap[int]:
        heap = MaxHeap()

        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.insert(4)

        return heap

    def build_min_heap_one(self):
        heap = MinHeap()

        heap.insert(3)
        heap.insert(1)
        heap.insert(4)
        heap.insert(2)

        return heap
