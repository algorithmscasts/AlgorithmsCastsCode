"""
Problem: https://leetcode.com/problems/game-of-life/
Topics: Matrix, Simulation
Difficulty: Medium
Youtube Explanation: https://youtu.be/43n7YmoTjf4
"""
class Solution:
    def gameOfLife(self, board):
        def live_nei_count(board, i, j):
            count = 0
            d = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

            for (di, dj) in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 1:
                    count += 1
            return count

        rows, cols = len(board), len(board[0])
        live, dead = [], []
        for i in range(rows):
            for j in range(cols):
                live_count = live_nei_count(board, i, j)
                cell = board[i][j]
                if cell == 1:
                    if live_count < 2 or live_count > 3:
                        dead.append((i, j))
                if cell == 0 and live_count == 3:
                    live.append((i, j))

        for (i, j) in dead:
            board[i][j] = 0

        for (i, j) in live:
            board[i][j] = 1


    def gameOfLifeSol2(self, board):

        def live_nei_count(board, i, j):
            count = 0
            d = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

            for (di, dj) in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] in [1, 3]:
                    count += 1
            return count

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                live_count = live_nei_count(board, i, j)
                cell = board[i][j]

                if cell == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = 3  # became dead
                elif cell == 0 and live_count == 3:
                    board[i][j] = 2  # became live

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
