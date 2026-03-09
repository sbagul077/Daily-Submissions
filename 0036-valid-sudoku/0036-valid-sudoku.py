class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board is None or len(board) == 0:
            return False
        
        # rows
        for i in range(len(board)):
            rows = [False for row in range(9)]
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if rows[int(board[i][j]) - 1] == True:
                        return False
                    rows[int(board[i][j]) - 1] = True
        
        #Column check

        for j in range(len(board[0])):
            cols = [False for col in range(9)]
            for i in range(len(board)):
                if board[i][j] != ".":
                    if cols[int(board[i][j]) - 1] == True:
                        return False
                    cols[int(board[i][j]) - 1] = True
        

        #Block check

        for b in range(9):
            blocks = [False for block in range(9)]
            for i in range(b // 3 * 3, b // 3 * 3 + 3):
                for j in range(b % 3 * 3, b % 3 * 3 + 3):
                    if board[i][j] != ".":
                        if blocks[int(board[i][j]) - 1] == True:
                            return False
                        blocks[int(board[i][j]) - 1] = True

        return True

# //Time Complexity: O(1) - 9x9 grid means constant time.
# //Space Complexity: O(1) - Only 27 sets used (constant space), each holds up to 9 elements.
# Iterate rows, cols to check for duplicates and maintain a array boolean array of length 9
# for blocks since its a 3 x 3 block. if we take division for block number and divide by 3 and then multiple by 3 we get the exact row of the current block and take mod for columns

# row = (b / 3 * 3) - (b / 3 * 3 + 3)
# col = (b % 3 * 3) - (b % 3 * 3 + 3)