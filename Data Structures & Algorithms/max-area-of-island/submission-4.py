class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r <0 or c <0 or r>=rows or c>=cols:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row,col)
                    max_area = max(max_area, area)
        
        return max_area
        