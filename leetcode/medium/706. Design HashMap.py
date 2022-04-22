"""
Problem: https://leetcode.com/problems/design-hashmap/
Topics: Array, Hash Table, Linked List, Design, Hash Function
Difficulty: Medium
Youtube Explanation: https://youtu.be/2jpkyVaKhig
"""
class MyHashMap:

    def __init__(self):
        self.values = [-1] * (10 ** 6 + 1)

    def put(self, key, value):
        self.values[key] = value

    def get(self, key):
        return self.values[key]

    def remove(self, key):
        self.values[key] = -1


class MyHashMapSol2:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]  # list of (key, value )

    def put(self, key, value):
        bucket = self.bucket(key)
        i = self.find(bucket, key)
        if i != -1:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def get(self, key):
        bucket = self.bucket(key)
        i = self.find(bucket, key)
        if i != -1:
            return bucket[i][1]
        return -1

    def remove(self, key):
        bucket = self.bucket(key)
        i = self.find(bucket, key)
        if i != -1:
            del bucket[i]

    def find(self, bucket, key):
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return -1

    def bucket(self, key):
        return self.buckets[key % self.size]


class ListNode:
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt


class MyHashMapSol3:

    def __init__(self):
        self.size = 1000
        self.buckets = [ListNode(-1, -1) for _ in range(self.size)]  #

    def put(self, key, value):
        idx = self.index(key)
        pred = self.findPredNode(self.buckets[idx], key)  # node before key
        if pred.next and pred.next.key == key:
            pred.next.val = value
        else:
            pred.next = ListNode(key, value)

    def get(self, key):
        idx = self.index(key)
        pred = self.findPredNode(self.buckets[idx], key)
        if pred.next and pred.next.key == key:
            return pred.next.val
        return -1

    def remove(self, key):
        idx = self.index(key)
        pred = self.findPredNode(self.buckets[idx], key)
        if pred.next and pred.next.key == key:
            pred.next = pred.next.next

    def index(self, key):
        return key % self.size

    def findPredNode(self, start, key):
        curr = start
        while curr.next and curr.next.key != key:
            curr = curr.next
        return curr
