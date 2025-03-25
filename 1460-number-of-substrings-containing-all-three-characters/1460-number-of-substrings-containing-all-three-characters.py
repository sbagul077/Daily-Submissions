class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        list = [-1, -1, -1]
        total = 0

        for i in range(len(s)):
            list[ord(s[i]) - ord("a")] = i

            total += 1 + min(list)
        
        return total