class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        time = [[math.inf] * cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    self.dfs(grid, time, i, j, 0)
        
        max_time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and time[i][j] == math.inf:
                    # print(time)
                    return -1
                if time[i][j] != math.inf:
                    max_time = max(max_time, time[i][j])
        # print(time)
        return max_time
    
    def dfs(self, grid, time , row, col, current_time):
        rows = len(grid)
        cols = len(grid[0])

        #boudary check
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 
        
        #if empty cell
        if grid[row][col] == 0:
            return
        
        #if already visited with smaller time -> stop
        if time[row][col] <= current_time:
            return
        
        time[row][col] = current_time

        #explore directions
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        for dr, dc in dirs:
            self.dfs(grid, time, row + dr, col + dc, current_time + 1)
