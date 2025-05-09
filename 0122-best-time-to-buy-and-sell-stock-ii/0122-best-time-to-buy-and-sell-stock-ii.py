class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minShare = float("inf")

        for price in prices:
            if price > minShare:
                maxProfit += price - minShare
                minShare = price
            else:
                minShare = price
        
        return maxProfit
    
#Time Complexity: O(n)
#Space Complexity: O(1)
