class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return list()
        
        result = [0] * len(nums)
        result[0] = 1
        
        n = len(nums)
        rp = 1
        #left to right pass
        for i in range(1, n):
            rp = rp * nums[i - 1]
            result[i] = rp         

        rp = 1
        
        for i in range(n - 2, -1, -1):
            rp = rp * nums[i + 1]
            result[i] = result[i] * rp
        
        return result

#2 pass
#Time Complexity: O(n)
#Space Complexity: O(1)