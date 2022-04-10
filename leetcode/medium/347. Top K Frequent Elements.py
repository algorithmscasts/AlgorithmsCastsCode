import collections
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, A, k):
        return [x for x, _ in Counter(A).most_common(k)]

    def topKFrequentSol2(self, A, k):
        c = Counter(A)
        h = []
        for value, occ in c.items():
            heapq.heappush(h, (-occ, value))

        return [heapq.heappop(h)[1] for _ in range(k)]

    def topKFrequentSol3(self, A, k):
        m = collections.defaultdict(int)
        for x in A:
            m[x] += 1
        h = []
        for value, occ in m.items():
            heapq.heappush(h, (-occ, value))

        return [heapq.heappop(h)[1] for _ in range(k)]

    def topKFrequentSol4(self, A, k):
        m, h = collections.defaultdict(int), []
        for x in A:
            m[x] += 1
        for value, occ in m.items():
            heapq.heappush(h, (-occ, value))

        return [heapq.heappop(h)[1] for _ in range(k)]

    def topKFrequentSol5(self, A, k):
        count = Counter(A)
        buckets = [[] for _ in range(len(A) + 1)]

        for key, freq in count.items():
            buckets[freq].append(key)

        flat_lst = [x for lst in buckets for x in lst]
        return flat_lst[::-1][:k]