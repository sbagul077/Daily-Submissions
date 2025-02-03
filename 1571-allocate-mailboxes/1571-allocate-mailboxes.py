class Solution:  # 575 ms, faster than 57.25%
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                medianPos = houses[(i + j) // 2]
                for m in range(i, j + 1):
                    costs[i][j] += abs(medianPos - houses[m])

        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n: return 0
            if k == 0 or i == n: return math.inf
            ans = math.inf
            for j in range(i, n):
                cost = costs[i][j]  # Try to put a mailbox among house[i:j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)