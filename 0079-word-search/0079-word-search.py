class Solution:
    dirs = []
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        m = len(board)
        n = len(board[0])
        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(m):
            for j in range(n):                
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
    
    def dfs(self, board, word, row, col, index):
        #base
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] == "#":
            return False

        if index == len(word):
            return True

        if word[index] == board[row][col]:
            if index == len(word) - 1:
                return True
            ch = board[row][col]
            board[row][col] = "#"

            for d in self.dirs:
                nr = d[0] + row
                nc = d[1] + col
                
                if self.dfs(board, word, nr, nc, index + 1):
                    return True
            board[row][col] = ch
        
        return False