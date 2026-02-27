class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None or len(mat) == 0:
            return mat

        m = len(mat)
        n = len(mat[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i,j])
                else:
                    mat[i][j] = -1
        distance = 1
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                for d in dirs:
                    nr = d[0] +  curr[0]
                    nc = d[1] + curr[1]        
                    if nr >= 0 and nc >= 0 and nr < m and nc < n  and mat[nr][nc] == -1:
                        mat[nr][nc] = distance
                        queue.append([nr, nc])
            distance += 1
        
        return mat



#BFS
#Time Complexity: O(M * N)
#Space Complexity: O(M * N)