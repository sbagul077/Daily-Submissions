class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if height is None or len(height) == 0:
            return result
        
        lw = 0
        rw = 0
        left = 0
        right = len(height) - 1
        
        while left <= right:
            if lw <= rw:
                if height[left] < lw:
                    result += lw - height[left]
                else:
                    lw = height[left]
                
                left += 1
            else:
                if rw > height[right]:
                    result += rw - height[right]
                else:
                    rw = height[right]
                right -= 1
        
        return result
    
#Time Complexity :O(n)
#Space Complexity: O(1)