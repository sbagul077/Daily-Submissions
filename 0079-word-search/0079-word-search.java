class Solution {
    int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int m;
    int n;
    public boolean exist(char[][] board, String word) {
        if(board.length == 0 || board == null){
            return false;
        }

        m = board.length;
        n = board[0].length;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(backtrack(board, word, i, j, 0)){
                    return true;
                }
            }
        }

        return false;
    }

    private boolean backtrack(char[][] board, String word, int i, int j, int index){
        //base
        if(i < 0 || j < 0 || i == m || j == n || board[i][j] == '#'){
            return false;
        }

        if(index == word.length()) return true;

        if(word.charAt(index) == board[i][j]){
            if(index == word.length() - 1) return true;

            //action
            char ch = board[i][j];
            board[i][j] = '#';

            for(int[] dir: dirs){
                int nr = dir[0] + i;
                int nc = dir[1] + j;

                if(backtrack(board, word, nr, nc, index + 1) == true){
                    return true;
                }
            }
            board[i][j] = ch;         
        }

        return false;
    }
}


// # For Loop Recursion Backtracking
// # Time Complexity: O(M*N*4^L). Where L is the lenght of the word
// # Space Complexity: O(L). Where L is the length of the word