class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minShare = float("inf")
        
        result = float("-inf")
        
        for price in prices:
            minShare = min(minShare, price)
            
            result = max(result, price - minShare)
        
        return result

#Sliding Windows
#Time Complexity: O(n)
#Space Complexity: O(1)