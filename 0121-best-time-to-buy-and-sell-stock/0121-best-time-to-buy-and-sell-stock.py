class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #left = buy
        right = 1  #right = sell
        maxProfit = 0
        
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right += 1
        
        return maxProfit
    
#Sliding Window
#Time Complexity: O(n)
#Space Complexity: O(1)