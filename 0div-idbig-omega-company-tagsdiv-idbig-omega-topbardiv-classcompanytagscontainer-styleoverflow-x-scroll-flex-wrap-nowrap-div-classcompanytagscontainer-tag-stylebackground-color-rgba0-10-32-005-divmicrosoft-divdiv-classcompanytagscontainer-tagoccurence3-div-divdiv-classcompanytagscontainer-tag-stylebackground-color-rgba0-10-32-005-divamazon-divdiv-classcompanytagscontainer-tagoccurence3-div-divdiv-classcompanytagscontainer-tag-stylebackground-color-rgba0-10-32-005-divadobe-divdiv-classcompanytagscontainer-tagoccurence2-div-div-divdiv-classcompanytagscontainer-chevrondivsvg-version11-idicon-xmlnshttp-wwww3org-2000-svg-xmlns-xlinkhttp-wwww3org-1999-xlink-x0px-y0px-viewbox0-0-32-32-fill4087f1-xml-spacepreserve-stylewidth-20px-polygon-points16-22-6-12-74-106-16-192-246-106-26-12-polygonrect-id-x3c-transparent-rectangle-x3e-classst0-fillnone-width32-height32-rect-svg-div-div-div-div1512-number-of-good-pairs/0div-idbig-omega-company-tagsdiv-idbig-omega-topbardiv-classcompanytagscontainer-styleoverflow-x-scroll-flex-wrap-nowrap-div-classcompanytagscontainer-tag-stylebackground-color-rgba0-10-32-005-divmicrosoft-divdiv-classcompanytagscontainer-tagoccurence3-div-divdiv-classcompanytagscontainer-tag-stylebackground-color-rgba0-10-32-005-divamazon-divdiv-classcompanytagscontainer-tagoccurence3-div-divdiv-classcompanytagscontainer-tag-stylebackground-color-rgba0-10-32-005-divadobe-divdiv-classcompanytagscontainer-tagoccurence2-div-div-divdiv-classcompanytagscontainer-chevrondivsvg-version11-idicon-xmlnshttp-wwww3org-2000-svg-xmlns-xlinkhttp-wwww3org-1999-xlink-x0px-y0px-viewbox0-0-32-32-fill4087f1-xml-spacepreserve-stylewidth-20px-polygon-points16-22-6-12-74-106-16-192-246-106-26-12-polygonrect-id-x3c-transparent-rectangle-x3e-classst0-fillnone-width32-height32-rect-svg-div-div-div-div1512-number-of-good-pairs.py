class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = dict()
        result = 0
        

        for num in nums:
            result += hashMap.get(num, 0)
            if num not in hashMap.keys():
                hashMap[num] = 1 
            else:                
                hashMap[num] = hashMap.get(num, 0) + 1
            
        return result

#Maths
#Time Complexity: O(n)
#Space Complexity: O(n)