class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        m = len(haystack)
        n = len(needle)

        i = 0 #source
        j = 0 #pattern
        lps = self.lps(needle)

        while i < m:
            print(i,j)
            if haystack[i] == needle[j]:
                # print("this")
                i += 1
                j += 1                
                if j == n:
                    return i - n
            elif haystack[i] != needle[j] and j > 0:
                j = lps[j-1]
                
            elif haystack[i] != needle[j] and j == 0:
                i += 1
        
        return -1
    
    def lps(self, needle):
        lps = [0] * len(needle)
        # lps = [0 for i in range(len(needle))]
        i = 1
        j = 0
        while(i < len(needle)):
            if needle[i] == needle[j]:
                j+= 1
                lps[i] = j
                i+= 1
            elif needle[i] != needle[j] and j > 0:
                j = lps[j- 1]
            else:
                lps[i] = 0
                i += 1
            
        return lps


#KMP Algorithm
#Time Complexity: O(m + n)
#Space Complexity: O(n)