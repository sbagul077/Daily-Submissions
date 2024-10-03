class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if pattern is None or len(pattern) == 0 or s is None or len(s) == 0:
            return False
        
        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False
        
        pMap = dict()
        sMap = dict()        
        # print(s)
        for i in range(len(pattern)):
            char = pattern[i]
            
            if char in pMap.keys():
                if pMap.get(char) != s[i]:
                    return False
            else:
                pMap[char] = s[i]
            
            if s[i] in sMap:
                if sMap.get(s[i]) != char:
                    return False
            else:
                sMap[s[i]] = char
                
        return True
                    
                
                