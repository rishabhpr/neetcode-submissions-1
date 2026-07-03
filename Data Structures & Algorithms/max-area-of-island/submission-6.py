class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0
        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        def dfs(r,c):
            if not 0<=r <rows or not 0<= c < cols:
                return 0
            
            if (r,c) in visited or grid[r][c] == 0:
                return 0
            
            # process the node
            visited.add((r,c))
            area = 1

            for dr,dc in directions:
                area += dfs(r+dr, c+dc)
            
            return area
        
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] ==1:
                    max_area = max(max_area, dfs(row,col))
        
        return max_area



                

        