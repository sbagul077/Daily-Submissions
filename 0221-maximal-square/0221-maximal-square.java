class Solution {
    public int maximalSquare(char[][] matrix) {
        if(matrix == null || matrix.length == 0){
            return 0;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int max = 0;
        int prev = 0;
        int diagUp = 0;
        int[] dp = new int[n + 1];

        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                prev = dp[j];
                if(matrix[i-1][j-1] == '1'){
                    // dp[i][j] = 1 + Math.min(dp[i][j - 1], Math.min(dp[i-1][j], dp[i-1][j-1]));
                    dp[j] = 1 + Math.min(dp[j-1], Math.min(dp[j], diagUp));
                    max = Math.max(max, dp[j]);
                }
                else{
                    dp[j] = 0;
                }
                diagUp = prev;
            }
        }

        return max * max;
    }
}

// 1D array bottom up DP
// Time Complexity: O(m *n)
// Space Complexity: O(n)