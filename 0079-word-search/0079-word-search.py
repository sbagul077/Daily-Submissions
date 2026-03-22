class Solution:
    m = 0
    n = 0
    dirs = []
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        
        self.dirs = [[0, 1], [0, -1], [1, 0],[-1, 0]]
        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):

                if self.backtrack(board, word, i, j, 0):
                    return True
        
        return False

    def backtrack(self, board: List[List[str]], word: str, i: int, j: int, index: int) -> bool:
        #base case
        if i < 0 or j < 0 or i == self.m or j == self.n or board[i][j] == "#":
            return False
        
        if index == len(word):
            return True

        if(word[index] == board[i][j]):
            if index == len(word) - 1:
                return True
            char = board[i][j]
            board[i][j] = "#"

            for d in self.dirs:
                nr = d[0] + i
                nc = d[1] + j

                if self.backtrack(board, word, nr, nc, index + 1):
                    return True
                
            board[i][j] = char
        return False

# For Loop Recursion Backtracking
# Time Complexity: O(M*N*4^L). Where L is the lenght of the word
# Space Complexity: O(L). Where L is the lenght of the word