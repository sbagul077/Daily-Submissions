class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxHeight = float("-inf")
        
        if height is None or len(height) == 0:
            return maxHeight
        
        low = 0
        high = len(height) - 1
        
        while low < high:
            
            maxHeight = max(maxHeight, min(height[high], height[low]) * (high - low))
            
            # print(maxHeight, min(height[high], height[low]) * (high - low))
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
        
        return maxHeight

#Time Complexity: O(n)
#Space Complexity: O(1)