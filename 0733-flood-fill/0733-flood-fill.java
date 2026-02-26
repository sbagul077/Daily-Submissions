class Solution {
    int[][] dirs;
    int prevColor;
    int m, n;
    int[][] image;
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
        this.dirs = new int[][]{{-1,0},{1,0},{0,1},{0,-1}};
        this.prevColor = image[sr][sc];
        this.m = image.length;
        this.n = image[0].length;
        this.image = image;
        if(prevColor == color){
            return image;
        }
        // this.image[sr][sc] = color;

        dfs(sr, sc, color);

        return this.image;
    }

    private void dfs(int sr, int sc, int color){
        // System.out.println(this.image[sr][sc]);
        if(sr < 0 || sc < 0 || sr >= m || sc >= n || this.image[sr][sc] != prevColor){
            return;
        }

        this.image[sr][sc] = color;
        
        for(int[] dir: dirs){
            int nr = dir[0] + sr;
            int nc = dir[1] + sc;

            dfs(nr, nc, color);
        }
    }
}

// DFS
// Time Complexity: O(N)
// Space Complexity: O(N)