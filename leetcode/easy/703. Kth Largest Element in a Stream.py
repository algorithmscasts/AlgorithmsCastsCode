"""
Problem: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Topics: Priority Queue, Sorted list
Difficulty: Easy
Youtube Explanation:
"""
import heapq
from bisect import bisect


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.pq = nums
        heapq.heapify(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)

        return self.pq[0]


class KthLargestSol2:

    def __init__(self, k: int, nums):
        self.k = k
        self.pq = nums
        heapq.heapify(self.pq)
        while len(self.pq) > k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif val > self.pq[0]:
            heapq.heapreplace(self.pq, val)
        return self.pq[0]


class KthLargestSol3:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        while len(self.nums) > self.k:
            self.nums.pop(0)

        return self.nums[0]
