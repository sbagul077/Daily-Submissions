class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        result = 0
        hashMap = dict()
        
        
        for i in range(len(s)):
            char = s[i]
            
            if char in hashMap.keys():
                slow =  max(slow, hashMap.get(char) + 1)

            result = max(result, i - slow + 1)
            
            hashMap[char] = i 
        
        return result
            
            
            
