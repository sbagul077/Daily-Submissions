class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        self.max = 0
        prevMax = 0
        hashMap = dict()
        
        for num in nums:
            
            hashMap[num] = hashMap.get(num, 0) + 1
            
            if prevMax < hashMap.get(num):
                prevMax = hashMap.get(num)
                self.max = num
        
        return self.max

#HashMap
#Time Complexity: O(n)
#Space Complexity: O(n)