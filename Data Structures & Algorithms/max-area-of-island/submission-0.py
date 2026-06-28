class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,col=len(grid),len(grid[0])
        def dfs(r,c):
            if(r>=rows or r<0 or c>=col or c<0 or grid[r][c]==0):
                return 0
            grid[r][c]=0
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        m=0
        for r in range(rows):
            for c in range(col):
                
                if grid[r][c]==1:
                    d=dfs(r,c)
                    if (d>m):
                        m=d
        return m
