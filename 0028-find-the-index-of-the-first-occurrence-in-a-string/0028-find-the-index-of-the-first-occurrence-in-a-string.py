class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or len(haystack) == 0 or needle is None or len(haystack) ==0:
            return -1
        
        m = len(haystack)
        n = len(needle)

        for i in range(m):
            if haystack[i] == needle[0]:
                k = i
                j = 0
                while k < m and j < n:
                    if haystack[k] == needle[j]:
                        k += 1
                        j += 1
                    else:
                        break
                
                    if j == n:
                        return i
        
        return -1

#Brute Force
#Time Complexity: O((m-n) * n)
#Space Complexity: O(1)
                    

