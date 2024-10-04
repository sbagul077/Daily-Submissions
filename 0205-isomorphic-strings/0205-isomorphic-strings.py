class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s is None or len(s) == 0 or t is None or len(t)==0:
            return False
        
        sMap = dict()
        tMap = dict()
        
        for i in range(0, len(s)):
            sChar = s[i]
            tChar = t[i]
            
            if sChar in sMap.keys():
                # print(sChar, sMap)
                if sMap.get(sChar) != t[i]:
                    return False
            else:
                sMap[sChar] = tChar
            
            if tChar in tMap.keys():
                # print(tChar, tMap)
                if tMap.get(tChar) != s[i]:
                    return False
            else:
                tMap[tChar] = sChar
        
        return True
    
    
                    