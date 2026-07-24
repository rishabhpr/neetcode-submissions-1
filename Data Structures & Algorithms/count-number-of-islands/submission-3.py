class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row,col):
            if row < 0 or row >= len(grid):
                return

            if col < 0 or col >= len(grid[0]):
                return
            
            if grid[row][col] == "0":
                return
            
            if grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)
                return
            
        islands = 0

        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands +=1
                    dfs(r,c)

        return islands


        