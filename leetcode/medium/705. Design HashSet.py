class MyHashSet:

    def __init__(self):
        self.values = [False] * (10**6 + 1)

    def add(self, key):
        self.values[key] = True

    def remove(self, key):
        self.values[key] = False

    def contains(self, key):
        return self.values[key]


class MyHashSetSol2:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        if not self.contains(key):
            idx = self.index(key)
            self.buckets[idx].append(key)

    def remove(self, key):
        if self.contains(key):
            idx = self.index(key)
            self.buckets[idx].remove(key)

    def index(self, key):
        return key % self.size

    def contains(self, key):
        idx = self.index(key)
        return key in self.buckets[idx]
