class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        time=[[float('inf')]*cols for _ in range(rows)]
        def dfs(r,c,t):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 
            if grid[r][c]==0:
                return
            if t>=time[r][c]:
                return
            time[r][c]=t
            dfs(r+1,c,t+1)
            dfs(r-1,c,t+1)
            dfs(r,c+1,t+1)
            dfs(r,c-1,t+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    dfs(r,c,0)
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    if time[r][c]==float('inf'):
                        return -1
                    res=max(res,time[r][c])
        return res
                    