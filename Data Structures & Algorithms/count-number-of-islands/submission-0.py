
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visited=set()
        islands=0

        def bfs(r,c):
            queue=deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                i,j=queue.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if i+dr in range(rows) and j+dc in range(cols) and grid[i+dr][j+dc]=="1" and (i+dr,j+dc) not in visited:
                        queue.append((i+dr,j+dc))
                        visited.add((i+dr,j+dc))                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands
                


        
