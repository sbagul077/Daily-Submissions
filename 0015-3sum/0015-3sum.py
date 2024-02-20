class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        
        if nums is None or len(nums) == 0:
            return result
        
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            if nums[i] > 0:
                break
            
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                currSum = nums[i] + nums[low] + nums[high]
                
                if currSum < 0:
                    low += 1
                  
                elif currSum > 0:
                    high -= 1                   
                else:
                    
                    li = [nums[i], nums[low], nums[high]]
                    result.append(li)
                    low += 1
                    
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    
                    high -= 1                    
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                    
        return result
    
# Two Pointers
#Time Complexity: O(n^2)
#Space Complexity: O(n)