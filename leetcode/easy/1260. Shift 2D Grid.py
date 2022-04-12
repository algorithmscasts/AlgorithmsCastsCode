"""
Problem: https://leetcode.com/problems/shift-2d-grid/
Topics: Matrix, Simulation
Difficulty: Easy
Youtube Explanation: https://www.youtube.com/watch?v=uG3jUf98r50
"""

import itertools


class Solution:
    """
        In one shift operation:
       1. Element at grid[i][j] moves to grid[i][j + 1].
       2. Element at grid[i][n - 1] moves to grid[i + 1][0].
       3. Element at grid[m - 1][n - 1] moves to grid[0][0].
    """

    def shiftGridSol2(self, grid, k):  # T.C: O(k*rows*cols), S.C: O(k*rows*cols)
        rows, cols = len(grid), len(grid[0])
        for _ in range(k):  # O(k)
            newGrid = [[0 for _ in range(cols)] for _ in range(rows)]
            # go over every cell and shift
            for i in range(rows):  # O(rows)
                for j in range(cols - 1):  # O(cols)
                    newGrid[i][j + 1] = grid[i][j]  # 1

            for i in range(rows - 1):  # 2 # O(rows)
                newGrid[i + 1][0] = grid[i][cols - 1]

            newGrid[0][0] = grid[rows - 1][cols - 1]  # 3

            grid = newGrid

        return grid

    def shiftGridSol2(self, grid, k):
        rows, cols = len(grid), len(grid[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        for j in range(cols):
            j2 = (j + k) % cols
            for i in range(rows):
                i2 = (i + ((j + k) // cols)) % rows
                res[i2][j2] = grid[i][j]
        return res

    def shiftGridSol3(self, grid, k):
        rows, cols = len(grid), len(grid[0])
        k %= rows * cols
        # 1. convert to 1d array
        values = list(itertools.chain(*grid))  # or sum(grid, [])
        # 2. shift k times
        arr_iter = iter(values[-k:] + values[:-k])
        # 3. convert back to a matrix
        return [[next(arr_iter)
                 for _ in range(cols)]
                for _ in range(rows)]  # or [nums[i:i+col] for i in range(0, len(nums), col)]
