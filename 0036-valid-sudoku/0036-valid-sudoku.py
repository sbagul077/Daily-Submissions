class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board is None or len(board) == 0:
            return False
        
        #row
        for i in range(9):
            row = [False for i in range(9)]
            for j in range(9):
                if board[i][j] != ".":
                    if row[int(board[i][j]) - 1]:
                        return False
                    
                    row[int(board[i][j]) - 1] = True
                    
        #row 
        # for i in range(9):
        #     row = [False for i in range(9)]
        #     for j in range(9):
        #         if board[i][j] != ".":
        #             if row[int(board[i][j]) - 1]:
        #                 return False
        #             row[int(board[i][j]) - 1] = True
        
        
        #column        
        for j in range(9):
            col = [False for j in range(9)]
            for i in range(9):
                if board[i][j] != ".":
                    if col[int(board[i][j]) - 1]:
                        return False
                    col[int(board[i][j]) - 1] = True
        #column
        # for j in range(9):
        #     col = [False for j in range(9)]
        #     for i in range(9):
        #         if board[i][j] != ".":
        #             if col[int(board[i][j]) - 1]:
        #                 return False
        #             col[int(board[i][j]) - 1] = True
        
        #block
        
        for b in range(9):
            block = [False for i in range(9)]
            for i in range((b//3) * 3, ((b // 3) * 3) + 3):
                for j in range((b % 3) * 3, ((b % 3) * 3) + 3):
                    if board[i][j] != ".":
                        if block[int(board[i][j]) - 1]:
                            return False
                        block[int(board[i][j]) - 1] = True
        
        return True
        
        
        
#         #block
        
#         for b in range(9):
#             block = [False for b in range(9)]
#             for i in range((b // 3) * 3, ((b // 3) * 3) + 3):
#                 for j in range((b % 3) * 3, (round(b % 3) * 3) + 3):
#                     if board[i][j] != ".":
#                         if block[int(board[i][j]) - 1]:
#                             return False
#                         block[int(board[i][j]) - 1] = True
        
#         return True
            
                    