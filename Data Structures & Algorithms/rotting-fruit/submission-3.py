class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # first pass
        # find fresh orange count
        # add all rotten locations to queue

        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        queue = deque()
        minutes = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count +=1
            
                elif grid[row][col] == 2:
                    queue.append((row,col))
        
        if fresh_count == 0:
            return 0
        
        # outer while loop runs each minute
        # inner loop tracks and updates fruits rotting in that minute
        while queue and fresh_count >0:
            counter = len(queue)
            for i in range(counter):
                r,c = queue.popleft()

                # process all next neighbors for cur r,c
                for dr,dc in directions:
                    if (0 <= r+dr< rows) and (0 <= c+dc < cols):
                        nbr = grid[r+dr][c+dc]
                        if nbr == 1:
                            grid[r+dr][c+dc] = 2
                            fresh_count -=1
                            queue.append((r+dr, c+dc))
                
            minutes +=1
        
        if fresh_count == 0:
            return minutes
        return -1


                






        