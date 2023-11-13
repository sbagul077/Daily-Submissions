class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if sorted(s) ==  sorted(t):
            return True
        else:
            return False
        
#         hashMapS = dict()
#         hashMapT = dict()
        
#         for idx in range(len(s)):
#             hashMapS[s[idx]] = hashMapS.get(s[idx], 0) + 1
#             hashMapT[t[idx]] = hashMapT.get(t[idx], 0) + 1
            
#         print(hashMapT, hashMapS)
            
        
#         for key in hashMapS.keys():
#             if hashMapS.get(key) != hashMapT.get(key, 0):
#                 return False
            
#         return True