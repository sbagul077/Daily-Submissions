class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0 
        if height is None or len(height) == 0:
            return result
        
        left, right = 0, len(height) - 1
        lw, rw = 0, 0
        
        while left <= right:
            if lw <= rw:
                if height[left] < lw:
                    result += lw - height[left]
                else:
                    lw = height[left]
                left += 1
            else:
                if height[right] < rw:
                    result += rw - height[right]
                else:
                    rw = height[right]
                right -= 1
        
        return result

#Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(1
