class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        
        for num in nums:
            hashSet.add(num)
            
        maxLen = 0
        
        for i in range(len(nums)):
            curr = nums[i]
            if curr - 1 not in hashSet:
                length = 0
                while (curr + length) in hashSet:
                    length += 1
                
                maxLen = max(maxLen, length)
        
        return maxLen

#Time Complexity: O(n)
#Space Complexity: O(n)
                    
                 
                
        
        
            
        