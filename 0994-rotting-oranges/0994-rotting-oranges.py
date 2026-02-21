class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or grid is None:
            return 0
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        dirs = [[0,1], [0, -1], [1, 0],[-1, 0]]
        countFresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    countFresh += 1
        
        if countFresh == 0:
            return 0
        
        minutes = 0
        while len(queue) != 0:
            size = len(queue)

            for i in range(size):
                currOrange = queue.popleft()

                for d in dirs:
                    nr = d[0] + currOrange[0]
                    nc = d[1] + currOrange[1]

                    if (nr >= 0 and nr < m) and (nc >= 0 and nc < n) and grid[nr][nc] == 1:
                        
                        grid[nr][nc] = 2
                        queue.append([nr, nc])
                        countFresh -= 1
            
            minutes += 1
        if countFresh == 0:
            return minutes -1

        return -1
        
#BFS
#Time Complexity: O(N)
#Space Complexity: O(N)