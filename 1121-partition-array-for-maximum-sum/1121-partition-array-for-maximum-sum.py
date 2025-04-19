class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if arr is None or len(arr) == 0:
            return 0
        
        size = len(arr)

        dp = [0 for i in range(size)]
        dp[0] = arr[0]

        for i in range(1, size):
            maximum = arr[i]
            for j in range(1, k + 1):
                if i - j + 1 >= 0:
                    maximum = max(maximum, arr[i - j + 1])
                    if i - j >= 0:
                        dp[i] = max(dp[i], maximum * j + dp[i - j])
                    else:
                        dp[i] = max(dp[i], maximum * j)
                j -= 1
        
        return dp[-1]
