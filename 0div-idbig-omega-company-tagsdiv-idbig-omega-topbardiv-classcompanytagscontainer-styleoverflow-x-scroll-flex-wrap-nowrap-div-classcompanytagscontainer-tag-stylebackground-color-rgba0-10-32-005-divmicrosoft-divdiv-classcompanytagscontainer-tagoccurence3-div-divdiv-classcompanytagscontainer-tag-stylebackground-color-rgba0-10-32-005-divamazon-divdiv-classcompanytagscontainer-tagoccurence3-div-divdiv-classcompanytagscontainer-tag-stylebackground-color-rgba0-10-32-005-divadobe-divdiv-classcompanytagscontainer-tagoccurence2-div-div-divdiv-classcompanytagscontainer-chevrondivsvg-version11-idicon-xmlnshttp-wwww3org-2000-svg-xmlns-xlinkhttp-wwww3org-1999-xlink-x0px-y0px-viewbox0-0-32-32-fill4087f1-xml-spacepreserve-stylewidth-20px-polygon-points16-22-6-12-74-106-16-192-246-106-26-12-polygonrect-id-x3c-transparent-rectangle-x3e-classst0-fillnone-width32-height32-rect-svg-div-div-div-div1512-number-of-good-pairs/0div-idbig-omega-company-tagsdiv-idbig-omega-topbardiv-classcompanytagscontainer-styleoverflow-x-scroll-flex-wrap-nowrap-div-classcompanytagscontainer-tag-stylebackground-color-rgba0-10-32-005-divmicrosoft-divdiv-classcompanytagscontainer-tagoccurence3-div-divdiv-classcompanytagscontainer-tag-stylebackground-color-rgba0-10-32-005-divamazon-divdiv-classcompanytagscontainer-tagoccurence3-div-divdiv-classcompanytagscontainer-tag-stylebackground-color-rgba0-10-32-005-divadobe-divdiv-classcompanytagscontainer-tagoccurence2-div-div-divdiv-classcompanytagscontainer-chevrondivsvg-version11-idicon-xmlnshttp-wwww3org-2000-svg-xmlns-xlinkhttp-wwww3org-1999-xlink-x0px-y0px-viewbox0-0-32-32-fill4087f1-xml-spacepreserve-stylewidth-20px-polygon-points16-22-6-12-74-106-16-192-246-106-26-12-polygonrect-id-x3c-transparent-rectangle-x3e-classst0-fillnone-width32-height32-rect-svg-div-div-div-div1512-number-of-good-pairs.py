class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = dict()
        result = 0
        

        for num in nums:
            
            if num in hashMap.keys():
                result += hashMap.get(num)
                hashMap[num] = hashMap.get(num, 0) + 1
            else:                
                hashMap[num] = 1
            
        return result

#HashMap
#Time Complexity: O(n)
#Space Complexity: O(n)