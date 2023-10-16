class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        
        return nums
    
    
#two pointers
#Time Complexity: O(n)
#Space Complexity: O(1)