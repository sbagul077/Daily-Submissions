class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if nums ==0 or len(nums) == 0:
            return 0

        hashMap = dict()

        for num in nums:
            if num not in hashMap.keys():
                hashMap[num] = 0
            
            hashMap[num] = hashMap.get(num) + 1
        
        for key, value in hashMap.items():
            if value == 1:
                return key
        return 0
#hashing
# Time Complexity: O(2n)
# Space Complexity: O(n)