class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visited=set()
        if row==0 and col==0:
            return False
        def bfs(r,c,i):
            if i==len(word):
                return True
            directions=[
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]]
            
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[i] or (r,c) in visited:
                return False
            visited.add((r,c))
            for dr, dc in directions:
                if bfs(r+dr, c+dc, i+1):
                    return True
            visited.remove((r,c))
            return False
 
        for r in range(row):
            for c in range(col):
                if bfs(r,c,0):
                    return True
        return False
        