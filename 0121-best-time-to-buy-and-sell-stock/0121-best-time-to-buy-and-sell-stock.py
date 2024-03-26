class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minShare = float("inf")
        maxP = float("-inf")
        
        for price in prices:
            minShare = min(minShare, price)
            
            maxP = max(maxP, price - minShare)
        
        return maxP

#Time Complexity: O(n)
#Space Complexity: O(1)
