class Solution:
    m = 0
    n = 0
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    count = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        if grid is None or self.m == 0:
            return 0

        self.count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.count += 1
                    self.dfs(grid, i, j)
        
        return self.count
    
    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        #base
        if row < 0 or col < 0 or row == self.m or col == self.n or grid[row][col] == '0':
            return

        #logic
        grid[row][col] = '0'

        for d in self.dirs:
            nr = d[0] + row
            nc = d[1] + col

            self.dfs(grid, nr, nc)

# DFS
# Time Complexity: O(2MN)
# Space Complexity: O(min(MN))