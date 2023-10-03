class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        result = 0
        
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    result += 1
                    
        return result

#Brute Force
#Time Complexity: O(n^2)
#Space Complexity: O(1)