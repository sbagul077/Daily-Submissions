class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        
        hashSet = set()
        count = 0
        
        for i in range(len(s)):
            if s[i] in hashSet:
                count += 2
                hashSet.remove(s[i])
            else:
                hashSet.add(s[i])
        
        if len(hashSet) != 0:
            count += 1
        
        return count

#TC: O(n)
#SC: O(n)
        