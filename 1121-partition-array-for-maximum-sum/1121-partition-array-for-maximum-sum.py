class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if arr is None or len(arr) == 0:
            return 0
        
        size = len(arr)
        dp = [0] * size
        dp[0] = arr[0]
        
        for i in range(1, size):
            self.max = dp[i]
            for j in range(1, k + 1):
                if i - j + 1 >= 0:
                    self.max = max(self.max, arr[i - j + 1]) #max between number of elements in the partitions window
                    if i - j >= 0: #check if dp[i] is not negative
                        dp[i] = max(dp[i], (self.max * j + dp[i - j]))
                    else:
                        dp[i] = self.max * j
        return dp[-1]
                        
#Bottom Up DP
#Time Complexity: O(n * k)
#Space Complexity: O(n)