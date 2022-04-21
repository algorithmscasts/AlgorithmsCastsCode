"""
Problem: https://leetcode.com/problems/design-hashset/
Topics: Array, Hash Table, Linked List, Design, Hash Function
Difficulty: Medium
Youtube Explanation: https://youtu.be/7a6pfH9Y3bk
"""

class MyHashSet:

    def __init__(self):
        self.values = [False] * (10 ** 6 + 1)

    def add(self, key):
        self.values[key] = True

    def remove(self, key):
        self.values[key] = False

    def contains(self, key):
        return self.values[key]

"""
N/bucketSize = K
"""
class MyHashSetSol2:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):  # O(bucketSize) = O(10^4)
        if not self.contains(key):  # O(bucketSize) = O(10^4)
            idx = self.index(key)
            self.buckets[idx].append(key)

    def remove(self, key):
        if self.contains(key):  # O(bucketSize) = O(10^4)
            idx = self.index(key)
            self.buckets[idx].remove(key)  # O(N/bucketSize = K) = O(K), see https://wiki.python.org/main/TimeComplexity

    def index(self, key):  # O(1)
        return key % self.size

    def contains(self, key):  # O(N/bucketSize)
        idx = self.index(key)
        return key in self.buckets[idx]  # O(bucketSize) = O(10^4)
