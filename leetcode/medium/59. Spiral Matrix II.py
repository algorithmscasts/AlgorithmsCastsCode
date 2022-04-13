class Solution:
    def generateMatrix(self, n):
        res = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        counter = 1
        x, y = 0, 0
        seen = set()

        while counter <= n * n:
            res[x][y] = counter
            seen.add((x, y))

            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                x, y = nx, ny
            else:
                d = (d + 1) % 4
                dx, dy = directions[d]
                x, y = x + dx, y + dy
            counter += 1

        return res

    def generateMatrixSol2(self, n):
        res = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d, counter = 0, 0, 0, 1

        while counter <= n * n:
            res[x][y] = counter

            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and res[nx][ny] == 0:
                x, y = nx, ny
            else:
                d = (d + 1) % 4
                dx, dy = directions[d]
                x, y = x + dx, y + dy

            counter += 1

        return res
