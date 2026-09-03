from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        count = 0

        def bfs(r, c):
            nonlocal count

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            visited.add((r,c))
            queue.append((r,c))

            while queue:
                x, y = queue.popleft()

                for dr, dc in directions:
                    nr, nc = x + dr, y + dc

                    if nr < 0 or nr >= row or nc < 0 or nc >= col:
                        count += 1

                    elif grid[nr][nc] == 0:
                        count += 1

                    elif grid[nr][nc] == 1 and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)

        return count