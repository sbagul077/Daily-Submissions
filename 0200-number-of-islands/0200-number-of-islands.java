class Solution {
    public int numIslands(char[][] grid) {
        if(grid == null || grid.length == 0){
            return 0;
        }

        int result = 0;
        Queue<int []> q = new LinkedList<>();
        int m = grid.length;
        int n = grid[0].length;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    dfs(grid, i, j, m, n);
                    result += 1;
                }
            }
        }
        
        return result;
    }

    public void dfs(char[][] grid, int row, int col, int m, int n){
            if(row < 0 || row >= m || col < 0 || col >= n || grid[row][col] != '1'){
                return;
            } 
            grid[row][col] = '0';
            int[][] dirs = new int[][] {{0,1}, {1, 0},{0, -1},{-1, 0}};
            for(int[] dir : dirs){
                int nr = dir[0] + row;
                int nc = dir[1] + col;
                dfs(grid, nr, nc, m, n);
            }
        }
}

//BFS 
// Time Complexity: O(m *n)
// Space Complexity: O(min(m*n))