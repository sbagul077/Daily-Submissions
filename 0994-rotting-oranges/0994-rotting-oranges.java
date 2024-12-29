class Solution {
    public int orangesRotting(int[][] grid) {
        if(grid == null || grid.length == 0){
            return 0;
        }

        int freshOranges = 0;
        int mins = 0;
        Queue<int []> q = new LinkedList<>();

        int m = grid.length; //row
        int n = grid[0].length; // col

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j ++){
                if(grid[i][j] == 2){
                    q.add(new int[]{i, j});
                }
                else if (grid[i][j] == 1){
                    freshOranges += 1;
                }
            }
        }

        if(freshOranges == 0){
            return 0;
        }

        int[][] dirs = {{0,1}, {1,0}, {-1,0}, {0,-1}};

        while(!q.isEmpty()){
            int size = q.size();

            for(int i =0; i < size; i++){
                int[] currOrange = q.poll();

                for(int[] dir : dirs){
                    int nr = dir[0] + currOrange[0];
                    int nc = dir[1] + currOrange[1];

                    if((nr >= 0 && nr < m) && (nc >= 0 && nc < n) && (grid[nr][nc] == 1)){
                        grid[nr][nc] = 2;
                        q.add(new int[] {nr, nc});
                        freshOranges -= 1;
                    }
                }
            }
            mins += 1;
        }

        if(freshOranges == 0){
            return mins - 1;
        }
        return -1;

    }
}