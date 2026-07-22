class Solution {
    public int maximalSquare(char[][] matrix) {
        if(matrix == null || matrix.length == 0){
            return 0;
        }

        int result = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        
        int[][]dp = new int[m+1][n+1];
        
        for(int i = 1; i < dp.length; i++){
            for(int j = 1; j < dp[0].length; j++){
                if(matrix[i-1][j-1] == '1'){
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i][j-1])) + 1;
                    result = Math.max(dp[i][j], result);
                }
                else{
                    dp[i][j] = 0;
                }
            }
        }
        System.out.println(Arrays.toString(dp));
        return result * result;
    }
}


//Brute Force
// Time Complexity: O(m*n)^2
// Space Complexity: O(1)