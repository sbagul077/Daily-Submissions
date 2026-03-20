class Solution {
    List<List<String>> result;
    boolean[][] board;
    public List<List<String>> solveNQueens(int n) {
        result = new ArrayList<>();
        board = new boolean[n][n];
        if(n == 0){
            return result;
        }
        
        dfs(0);
        return result;
    }

    private void dfs(int row){
        //base
        if(row == board.length){
            List<String> li = new ArrayList<>();
            for(int i = 0; i < board.length; i++){
                StringBuilder sb = new StringBuilder();
                for(int j = 0; j < board.length; j++){
                    if(board[i][j] == true){
                        sb.append('Q');
                    }else{
                        sb.append('.');
                    }
                }
                li.add(sb.toString()); 
            }
            
            result.add(li);
            return;
        }
        //logic

        for(int j = 0; j < board[0].length; j++){
            if (isSafe(row, j)){
                //action
                board[row][j] = true;
                //recurse
                dfs(row + 1);
                board[row][j] = false;
            }
        }
    }

    private boolean isSafe(int r, int c){

        //col check
        for(int row = 0; row < r; row++){
            if(board[row][c] == true){
                return false;
            }
        }

        //diag up left
        int row = r;
        int col = c;

        while(row >= 0 && col >= 0){
            if(board[row][col] == true){
                return false;
            }
            row--;
            col--;
        }

        row = r;
        col = c;

        //diag up right
        while(row >= 0 && col < board.length){
            if(board[row][col] == true){
                return false;
            }
            row--;
            col++;
        }
        return true;
    }
}