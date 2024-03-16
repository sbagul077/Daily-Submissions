class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        
        n = len(nums)
        maximum, count = 0, 0
        hashMap = {0 : -1}
        
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in hashMap:
                maximum = max(maximum, i - hashMap[count])
            else:
                hashMap[count] = i
        
        return maximum
    
# TC :O(n)
# SC: O(n)