class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        hashMap = dict()

        result = 0
        slow = 0

        for i in range(len(s)):
            char = s[i]

            if char in hashMap.keys():
                slow = max(slow, hashMap.get(char))
            
            result = max(result, i - slow + 1)

            hashMap[char] =  i + 1
    
        return result

#Two Pointers and hashing
# Time Complexity: O(n)
# Space Complexity: O(n)