class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = max(height)
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left],height[right]) * (right - left)
            if(area > max_area):
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            if (right-left) * max_height < max_area:
                return max_area
        return max_area