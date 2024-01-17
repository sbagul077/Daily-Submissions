class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        if nums is None or len(nums) == 0:
            return result
        
        arr1 = [1 for i in range(len(nums))]
        arr2 = [1 for i in range(len(nums))]
        rp = 1
        for i in range(1, len(nums)):
            arr1[i] = rp * nums[i - 1]
            rp *= nums[i - 1]
        
        rp = 1
        
        for i in range(len(nums) - 2, -1, -1):
            arr2[i] = rp * nums[i + 1]
            rp *= nums[i + 1]
            
        print(arr1, arr2)
        
        for i in range(len(arr1)):
            result[i] = arr1[i] * arr2[i]
        
        return result
                
# Arrays
#Time Complexity: O(2n)
#Space Complexity: O(2n)