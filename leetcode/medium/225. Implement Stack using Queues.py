"""
Problem: https://leetcode.com/problems/implement-stack-using-queues/
Topics: Stack, Design, Queue
Difficulty: Medium
Youtube Explanation:
"""
import collections


class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x):
        self.q2 = self.q1
        self.q1 = collections.deque()
        self.q1.append(x)

        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

class MyStackSol2:

    def __init__(self):
        self.q = collections.deque([])

    def push(self, x):
        self.q.append(x)
        n = len(self.q)
        for _ in range(n - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
