class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0:
            return 0
        
        left = 0
        right = len(height) - 1
        lw = 0
        rw = 0
        result = 0

        while left <= right:
            if lw <= rw:
                if lw > height[left]:
                    result += lw - height[left]
                    left += 1
                else:
                    lw = height[left]
                    left += 1
            else:
                if rw > height[right]:
                    result += rw - height[right]
                    right -= 1
                else:
                    rw = height[right]
                    right -= 1
        
        return result

