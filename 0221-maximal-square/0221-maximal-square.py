class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        
        m = len(matrix) #row
        n = len(matrix[0]) #cols
        result = float("-inf")

        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]))
                
                result = max(result, dp[i][j])
        
        return result * result
    
#DP 
#Time Complexity: O(m * n)
#Space Complexity: O(m * n)


