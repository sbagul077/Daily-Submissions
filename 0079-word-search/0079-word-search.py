class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(word, board, row, col, index):
            #base
            if row < 0 or col < 0 or row == m or col == n or board[row][col] == "#":
                return False
            
            if len(word) == index:
                return True
            
            if word[index] == board[row][col]:
                if index == len(word) - 1:
                    return True
                
                ch = board[row][col]
                board[row][col] = "#"

                for d in dirs:
                    nr = d[0] + row
                    nc = d[1] + col
                    if dfs(word, board, nr, nc, index + 1):
                        return True
                
                board[row][col] = ch
        
            return False

        for i in range(m):
            for j in range(n):
                if dfs(word, board, i, j, 0):
                    return True
                            
        return False
                    