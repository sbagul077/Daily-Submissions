class Solution:
    result = list()
    board = list()
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = list()
        if n == 0:
            return self.result
        
        self.board = [[False for i in range(n)] for j in range(n)]

        self.dfs(0)
        return self.result
    
    def dfs(self, row):
        #base
        if row == len(self.board):
            li = list()
            for i in range(len(self.board)):
                sb = list()
                # print(self.board[i])
                for j in range(len(self.board)):
                    if self.board[i][j] == True:
                        sb.append("Q")
                    else:
                        sb.append(".")
                li.append("".join(sb))
            
            self.result.append(li)          

        #logic
        for j in range(0,len(self.board)):
            # print(j)
            if self.isSafe(row, j):
                #Action
                self.board[row][j] = True
                # Recurse
                self.dfs(row + 1)
                #Backtrack
                self.board[row][j] = False
    

    def isSafe(self, r, c):

        for row in range(0, r):
            if self.board[row][c]:
                return False
        
        row = r
        col = c

        #diag up left
        while row >= 0 and col >= 0:
            if self.board[row][col] == True:
                return False

            row -= 1
            col -= 1
        
        row = r
        col = c
        #diag up right
        while row >= 0 and col < len(self.board):
            if self.board[row][col]:
                return False
            row -= 1
            col += 1

        return True

#DFS
# Time Complexity: O(n!)
# Space Complexity: (N * N)