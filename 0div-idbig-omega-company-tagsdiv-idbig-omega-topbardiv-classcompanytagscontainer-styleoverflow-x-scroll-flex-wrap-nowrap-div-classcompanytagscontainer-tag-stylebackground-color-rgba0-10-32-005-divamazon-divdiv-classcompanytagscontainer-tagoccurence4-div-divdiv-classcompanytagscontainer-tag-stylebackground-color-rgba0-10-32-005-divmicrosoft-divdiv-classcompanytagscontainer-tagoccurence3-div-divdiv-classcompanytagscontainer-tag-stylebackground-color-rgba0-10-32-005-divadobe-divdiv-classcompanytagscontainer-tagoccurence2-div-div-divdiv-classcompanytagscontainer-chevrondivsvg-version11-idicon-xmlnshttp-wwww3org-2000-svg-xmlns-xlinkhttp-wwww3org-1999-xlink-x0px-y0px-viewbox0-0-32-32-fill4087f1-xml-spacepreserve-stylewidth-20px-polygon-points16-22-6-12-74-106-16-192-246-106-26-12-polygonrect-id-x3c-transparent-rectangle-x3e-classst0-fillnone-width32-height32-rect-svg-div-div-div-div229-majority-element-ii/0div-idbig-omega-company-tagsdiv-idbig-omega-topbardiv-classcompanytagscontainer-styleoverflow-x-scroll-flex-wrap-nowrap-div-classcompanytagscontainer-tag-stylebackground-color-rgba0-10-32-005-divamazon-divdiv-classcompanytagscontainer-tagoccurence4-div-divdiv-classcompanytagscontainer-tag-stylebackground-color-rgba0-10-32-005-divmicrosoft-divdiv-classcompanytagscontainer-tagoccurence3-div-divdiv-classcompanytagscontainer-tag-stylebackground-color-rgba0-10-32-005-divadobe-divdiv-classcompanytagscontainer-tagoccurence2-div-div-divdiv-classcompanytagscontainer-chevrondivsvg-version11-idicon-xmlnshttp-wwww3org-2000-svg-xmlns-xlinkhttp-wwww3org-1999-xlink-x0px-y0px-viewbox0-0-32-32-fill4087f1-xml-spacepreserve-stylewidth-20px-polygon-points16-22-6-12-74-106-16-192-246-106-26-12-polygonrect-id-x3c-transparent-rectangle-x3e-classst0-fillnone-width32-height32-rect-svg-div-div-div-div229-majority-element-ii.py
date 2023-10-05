class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = dict()
        
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        
        
        n = len(nums) // 3
        result = []
        
        for key, value in hashMap.items():
            if value > n:
                result.append(key)
        
        return result
    
#HashMap
#Time Complexity: O(n)
#Space Complexity: O(n)