class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(r,c):
            if not 0 <= r < rows or not 0<= c< cols:
                return 
            
            if grid[r][c] == "0" or (r,c) in visited:
                return
            
            visited.add((r,c))

            for dr,dc in directions:
                dfs(r+dr, c+dc)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col)  not in visited:
                    count+=1
                    dfs(row,col)
        
        return count




        