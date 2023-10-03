class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = dict()
        result = 0
        
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for key in hashMap.keys():
            n = hashMap.get(key)
            
            result +=  n * (n - 1) // 2
        
        return result

#Maths
#Time Complexity: O(n)
#Space Complexity: O(n)