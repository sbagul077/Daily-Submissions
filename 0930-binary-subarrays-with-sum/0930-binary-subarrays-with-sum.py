class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        #count number of subarrays  where curSum <= x
        def helper(x):
            if x < 0:
                return 0
            
            res = 0
            left = 0
            curr = 0
            
            for right in range(len(nums)):
                curr += nums[right]
                
                while curr > x:
                    curr -= nums[left]
                    left += 1
                
                res += (right - left + 1)
                
            return res
        
        return helper(goal) - helper(goal - 1)
    
#Sliding Window
#Time Complexity: O(n)
#Space Complexity: O(1)