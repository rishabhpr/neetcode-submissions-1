class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        rotten = 0
        minutes = 0

        offset = [[-1,0], [1,0], [0,1], [0,-1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh +=1
                
                if grid[row][col] == 2:
                    queue.append((row,col))

        while queue and fresh > 0:
            layer = len(queue)
            for _ in range(layer):
                r,c = queue.popleft()

                for dr, dc in offset:
                    nr = r+dr
                    nc = c+dc

                    if nr<0 or nc<0 or nr>=rows or nc>=cols:
                        continue

                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -=1
                    queue.append((nr,nc))
            
            minutes +=1
        
        if fresh == 0:
            return minutes
        else:
            return -1






