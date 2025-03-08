class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lps = self.lowest_common_prefix_suffix(part)
        pattern_index_arr = [0 for _ in range(len(s) + 1)] # keep track of pattern for j part pointer
        st = [] #stack to keep s characters that we processed
        i = 0 # pointer for s
        j = 0 # pointer for part
        n = len(s)
        m = len(part)

        while i < n:
            st.append(s[i])
            
            if s[i] == part[j]:
                j += 1
                pattern_index_arr[len(st)] = j
                i += 1

                if j == m:
                    for k in range(m):
                        st.pop()
                    if len(st):
                        j = pattern_index_arr[len(st)]
                    else:
                        j = 0
            elif s[i] != part[j] and j > 0:
                # i -= 1
                j = lps[j - 1]
                st.pop()
            elif s[i] != part[j] and j == 0:
                pattern_index_arr[len(st)] = 0
                i += 1
        
        return "".join(st)

    def lowest_common_prefix_suffix(self, part):
        lps = [0 for i in range(len(part))]
        i = 1
        j = 0

        while i < len(part):
            if part[i] == part[j]:
                j += 1
                lps[i] = j
                i += 1
            elif part[i] != part[j] and  j > 0:
                j = lps[j - 1]
            elif part[i] != part[j] and j == 0:
                lps[i] = 0
                i += 1
        return lps
