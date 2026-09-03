class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        max_size=float('-inf')
        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visited.add((r,c))
            count=1

            while q:
                rw,cl=q.pop()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if 0 <= rw + dr < rows and 0 <= cl + dc < cols and grid[dr+rw][dc+cl]==1 and (dr+rw,dc+cl) not in visited:
                        print("Count:",count)
                        count+=1
                        visited.add((dr+rw,dc+cl))
                        q.append((dr+rw,dc+cl))
                        
                        
            return count


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    m=bfs(r,c)
                    if max_size<m:
                        max_size=m
            
        if(max_size==float('-inf')):
            return 0
        else: 
            return max_size
                
                
        