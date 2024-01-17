class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        if nums is None or len(nums) == 0:
            return result
        
        rp = 1
        for i in range(1, n):
            rp = rp * nums[i - 1]
            result[i] *= rp
        
        rp = 1
        
        for i in range(n - 2, -1, -1):
            
            rp = rp * nums[i + 1]
            result[i] *= rp

        print(result)
        return result
                
# Arrays
#Time Complexity: O(n)
#Space Complexity: O(1)