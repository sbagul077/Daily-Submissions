class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0  # pointer for g
        j = 0  # pointer for s
        
        while i < len(g):
            while j < len(s) and  g[i] > s[j]:
                j += 1
            
            if j < len(s):
                i += 1
                j += 1
            else:
                break
        
        return i
    
# Sorting and Two Pointers
# Time Complexity: O(nlogn + mlogm)
# Space Complexity :O(1)
                
                
            