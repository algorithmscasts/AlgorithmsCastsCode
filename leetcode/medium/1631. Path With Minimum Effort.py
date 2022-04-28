from collections import deque


class Solution:
    def minimumEffortPath(self, heights):
        R, C = len(heights), len(heights[0])

        def valid(i, j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i, j, threshold, visited):
            if i >= R or j >= C:
                return False
            if i == R - 1 and j == C - 1:
                return True

            visited.add((i, j))
            for (ni, nj) in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if valid(ni, nj) and (ni, nj) not in visited:
                    cost = abs(heights[i][j] - heights[ni][nj])
                    if cost <= threshold and dfs(ni, nj, threshold, visited):
                        return True
            return False

        def canReachEnd(k):
            visited = set()
            return dfs(0, 0, k, visited)

        lo, hi = 0, 10 ** 6
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if canReachEnd(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def minimumEffortPathSol2(self, heights):

        def valid(i, j):
            return 0 <= i < R and 0 <= j < C

        def canReachEnd(threshold):
            visited, q = {(0, 0)}, deque([(0, 0)])

            while q:
                i, j = q.popleft()

                if i == R - 1 and j == C - 1:
                    return True

                for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if valid(ni, nj) and abs(heights[i][j] - heights[ni][nj]) <= threshold and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append((ni, nj))
            return False

        R, C = len(heights), len(heights[0])
        lo, hi = 0, 10 ** 6
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if canReachEnd(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo