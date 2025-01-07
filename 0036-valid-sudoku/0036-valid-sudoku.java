class Solution {
    public boolean isValidSudoku(char[][] board) {
        if(board == null || board.length == 0){
            return false;
        }

        for(int i = 0; i < 9; i++){
            boolean[] row = new boolean[9];
            for(int j = 0; j < 9; j++){
                if(board[i][j] != '.'){
                    // System.out.println(board[i][j]);
                    // System.out.println(row[board[i][j] - '0' - 1]);
                    if((row[board[i][j]- '0' - 1]) == true){
                        return false;
                    }
                    row[board[i][j]- '0' - 1] = true;
                }
            }
        }

        for(int j = 0; j < 9; j++){
            boolean[] col = new boolean[9];
            for(int i= 0; i < 9; i++){
                if(board[i][j] != '.'){
                    // System.out.println(board[i][j] - '0' - 1);
                    // System.out.println(col[board[i][j] - '0' - 1]);
                    if (col[board[i][j] - '0' - 1] == true){
                        return false;
                    }
                    col[board[i][j] - '0' - 1] = true;
                }
            }
        }

        for(int b = 0; b < 9; b++){
            boolean[] li = new boolean[9];
            for(int i = (b / 3 * 3); i < (b/ 3 * 3 + 3); i++){
                for(int j = b % 3 * 3; j < b % 3 *3 + 3; j++){
                    if(board[i][j] != '.'){
                        if(li[board[i][j] - '1']){
                            return false;
                        }
                        li[board[i][j] - '0' - 1] = true;
                    }
                }
            }
        }
        return true;

    }
}