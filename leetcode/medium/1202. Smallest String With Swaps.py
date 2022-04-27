class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        p = [i for i in range(n)]

        def find(x):
            if p[x] != x:  # we haven't reached the root yet
                p[x] = find(p[x])  # keep going up until we reach it
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:  # if they are not in same component add them there
                p[px] = py

        # put pairs in same component
        for i, j in pairs:
            union(i, j)

        # construct a map from root of comp to content of component as str sorted in asc order of string
        comp_map = collections.defaultdict(list)
        for i in range(n):
            comp_map[find(i)].append(s[i])

        # sort content of each comp
        for k in comp_map.keys():
            comp_map[k].sort(reverse=True)

        # go through each comp and replace in order each s char with the first in its comp
        res = ""
        for i in range(n):
            res += comp_map[find(i)].pop()
        return res
