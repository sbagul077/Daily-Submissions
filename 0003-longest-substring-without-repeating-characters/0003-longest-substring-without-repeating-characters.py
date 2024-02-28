class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        
        slow = 0
        maxLen = 0 
        hashMap = dict()
        
        for i in range(len(s)):
            char = s[i]
            
            if char in hashMap.keys():
                slow = max(slow, hashMap.get(char))
            
            maxLen = max(maxLen, i - slow + 1)
            hashMap[char] = i + 1
        
        return maxLen
            
            
#Time Complexity: O(n)
#Space Complexity: O(n)