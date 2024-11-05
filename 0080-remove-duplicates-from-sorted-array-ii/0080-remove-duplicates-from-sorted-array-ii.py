class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow = 1
        n = len(nums)
        count = 1

        
        for fast in range(1,n):
            if nums[fast] == nums[fast - 1]:
                count += 1 
                    
            else:
                count = 1 
                
            if count < 3:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
        