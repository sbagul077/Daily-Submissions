class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        m = len(haystack)
        n = len(needle)

        i = 0
        # print("this")
        while i <= m - n:
            if haystack[i] == needle[0]:
                # print("this")
                j = 0
                k = i
                while j < n and k < m and haystack[k] == needle[j]:
                    j += 1
                    k += 1

                    if j == n:
                        return i
            
            i += 1
        
        return -1

# Time Complexity: O(m * n)
# Space Complexity: O(1)