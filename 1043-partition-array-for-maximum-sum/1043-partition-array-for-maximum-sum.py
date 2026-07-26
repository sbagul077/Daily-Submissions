class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if arr is None or len(arr) == 0:
            return 0

        dp = [0] * len(arr)
        dp[0] = arr[0]

        for i in range(1, len(dp)):
            maxEle = dp[i]

            for j in range(1, k + 1):
                if i - j + 1 < 0:
                    break
                
                maxEle = max(maxEle, arr[i - j + 1])

                if i - j >= 0:
                    dp[i] = max(dp[i], maxEle *  j + dp[i-j])
                else:
                    dp[i] = max(dp[i], maxEle * j)
        

        
        # return dp[len(arr) - 1]
        
        return dp[-1]

# // DP
# // #time complexity: O(n * k)
# // Space Complexity: O(n)