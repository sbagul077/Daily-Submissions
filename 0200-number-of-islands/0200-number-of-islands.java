class Solution {
    int m;
    int n;
    int[][] dirs;
    int count;
    public int numIslands(char[][] grid) {
        m = grid.length;
        n = grid[0].length;
        if(grid == null || m == 0){
            return 0;
        }

        dirs = new int[][]{{0, 1}, {0, -1},{1, 0},{-1, 0}};
        count = 0;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    count++;
                    dfs(grid, i, j);
                }

            }
        }

        return count;
    }

    private void dfs(char[][] grid, int row, int col){
        //base
        if(row < 0 || col < 0 || row >= m || col >= n || grid[row][col] == '0'){
            return;
        }
        //logic
        grid[row][col] = '0';

        for(int[] dir: dirs){
            int nr = dir[0] + row;
            int nc = dir[1] + col;

            dfs(grid, nr, nc);
        }
    }
}

//DFS 
// Time Complexity: O(2(M *N))
// Space Complexity: O(Min(M,N))