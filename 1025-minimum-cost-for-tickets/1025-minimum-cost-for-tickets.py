class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:        
        dp = [0 for i in range(days[-1] + 1)]

        for i in range(0, len(dp)):

            if i in days:
                one = dp[max(i - 1, 0)] + costs[0]
                seven = dp[max(i - 7, 0)] + costs[1]
                thirty = dp[max(i - 30, 0)] + costs[2]

                dp[i] = min(one, min(seven, thirty))
            else:
                dp[i] = dp[i - 1]
        # print(dp)
        return dp[-1]

