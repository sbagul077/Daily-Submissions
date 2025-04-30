class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s is None:
            return False
        
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        hashSet = set(wordDict)

        for i in range(len(s) + 1):
            j = 0
            while j < i:
                if dp[j] and s[j : i] in hashSet:
                    dp[i] = True
                    break
                j+= 1
        
        return dp[-1]

#DP
# Time Complexity: O(N^2)
#Space Complexity: O(n)