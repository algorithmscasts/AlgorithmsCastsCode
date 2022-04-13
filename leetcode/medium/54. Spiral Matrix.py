"""
Problem: https://leetcode.com/problems/spiral-matrix/
Topics: Matrix, Simulation
Difficulty: Medium
Youtube Explanation:
"""
class Solution:
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        start_row, end_row = 0, rows - 1
        start_col, end_col = 0, cols - 1

        res = []
        while start_row < rows or start_col < cols:
            if start_row <= end_row:
                for j in range(start_col, end_col + 1):
                    res.append(matrix[start_row][j])
            start_row += 1

            if start_col <= end_col:
                for i in range(start_row, end_row + 1):
                    res.append(matrix[i][end_col])
            end_col -= 1

            if start_row <= end_row:
                for j in range(end_col, start_col - 1, -1):
                    res.append(matrix[end_row][j])
            end_row -= 1

            if start_col <= end_col:
                for i in range(end_row, start_row - 1, -1):
                    res.append(matrix[i][start_col])
            start_col += 1

        return res

    def spiralOrderSol2(self, matrix):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(matrix), len(matrix[0])
        x, y, d = 0, 0, 0
        res, seen = [], set()

        while len(res) < rows * cols:
            res.append(matrix[x][y])
            seen.add((x, y))

            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen:
                x, y = nx, ny
            else:  # change direction
                d = (d + 1) % len(directions)
                dx, dy = directions[d]
                x, y = x + dx, y + dy

        return res

    def spiralOrderSol3(self, matrix):
        def transpose(matrix):
            if not matrix:
                return []
            rows, cols = len(matrix), len(matrix[0])
            t = [[0 for _ in range(rows)] for _ in range(cols)]

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    t[j][i] = matrix[i][j]

            return t

        res = []
        while matrix:
            first_row = matrix.pop(0)
            res.extend(first_row)

            matrix = list(reversed(transpose(matrix)))
        return res

    def spiralOrderSol4(self, matrix):
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res

    def spiralOrderSol5(self, matrix):
        if not matrix:
            return []
        first_row = matrix.pop(0)
        zm = list(zip(*matrix))
        new_matrix = [list(x) for x in zm[::-1]]
        return first_row + self.spiralOrder(new_matrix)

    def spiralOrderSol6(self, matrix):
        return matrix and matrix.pop(0) + self.spiralOrder([list(x) for x in list(zip(*matrix))[::-1]])
