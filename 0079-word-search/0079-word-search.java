class Solution {
    int[][] dirs = new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;

        // int[][] dirs = new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0) == true) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int row, int col, int index) {
        // base
        if (row < 0 || col < 0 || row == board.length || col == board[0].length || board[row][col] == '#') {
            return false;
        }
        if (index == word.length()) {
            return true;
        }

        if (board[row][col] == word.charAt(index)) {
            if (index == word.length()-1) {
                return true;
            }

            char ch = board[row][col];
            board[row][col] = '#';

            for (int[] dir : dirs) {
                int nr = dir[0] + row;
                int nc = dir[1] + col;
                if (dfs(board, word, nr, nc, index + 1) == true) {
                    return true;
                }
            }
            board[row][col] = ch;
        }
        return false;
    }
}