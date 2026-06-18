class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        count=0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=='1':
                    count=count+1
                    q=deque()
                    q.append((r,c))
                    while q:
                        row,col=q.popleft()
                        dir=[(-1,0),(1,0),(0,-1),(0,1)]
                        for dr,dc in dir:
                            next_row=row+dr
                            next_col=col+dc
                            if(0<=next_row<rows)and(0<=next_col<columns) and grid[next_row][next_col]=='1':
                                q.append((next_row,next_col))
                                grid[next_row][next_col]='0'
        return count
                    
    



        