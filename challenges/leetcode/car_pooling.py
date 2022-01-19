"""
Solution for LC#:1094 Car Pooling

https://leetcode.com/problems/car-pooling/
"""
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_load = [0] * 1001  # key universe in terms of distances: 0 km <= from, to <= 1000 km

        # compute the car's load on each start (add passengers)
        # and on each end (remove passengers)
        for people, start, finish in trips:
            trip_load[start] += people
            trip_load[finish] -= people

        # check if the current load exceeds the max capacity during the trips
        load = 0
        for people in trip_load:
            load += people

            if load > capacity:
                return False

        return True
