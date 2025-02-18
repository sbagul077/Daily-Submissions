class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashMap = dict()
        result = list()
        for i in range(len(s)):
            char = s[i]
            
            hashMap[char] = hashMap.get(char, 0) + 1
        
        for i in range(len(order)):
            char = order[i]
            if char in hashMap.keys(): 
                count = hashMap.get(char)
                while count > 0:
                    result.append(char)
                    count -= 1
                hashMap.pop(char)
        
        for key in hashMap.keys():
            count = hashMap.get(key)
            while count > 0:
                result.append(key)
                count -= 1        
     
        return "".join(result)
            
#Time Complexity: O(m + n)
#space Complexity: O(n). size of string s