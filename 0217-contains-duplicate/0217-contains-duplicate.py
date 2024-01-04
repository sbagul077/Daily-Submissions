class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()
        
        
        for i in nums:
            if i not in hashMap.keys():
                hashMap[i] = i
            else:
                return True
            
        return False
    

#HashMap
#Time Complexity: O(n)
#Space Complexity: O(n)