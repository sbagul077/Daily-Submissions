class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(1, n):
            for j in range(n):
                mid = matrix[i - 1][j]
                left = matrix[i - 1][j - 1] if j > 0 else float("inf")
                right = matrix[i - 1][j + 1] if j < n - 1 else float("inf")
                matrix[i][j] = matrix[i][j] + min(mid, left, right)
        
        return min(matrix[-1])
                
# Bottom UP DP
# Time Complexity: O(n)
#Space Complexity: O(n)