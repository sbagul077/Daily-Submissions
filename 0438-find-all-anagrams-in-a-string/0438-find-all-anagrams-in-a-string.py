class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashMap = dict()
        result = []
        for char in p:
            hashMap[char] = hashMap.get(char, 0) + 1
        
        match = 0
        for i in range(len(s)):
            char = s[i]

            if char in hashMap.keys():
                cnt = hashMap.get(char)
                cnt -= 1
                hashMap[char] = cnt
                if(cnt == 0):
                    match += 1
            
            if i >= len(p):
                if s[i - len(p)] in hashMap.keys():
                    cnt = hashMap.get(s[i - len(p)])
                    cnt += 1
                    hashMap[s[i - len(p)]] = cnt
                    if cnt == 1:
                        match -= 1
            
            if match == len(hashMap):
                result.append(i - len(p) + 1)
        
        return result