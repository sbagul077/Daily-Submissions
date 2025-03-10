class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        if(len(p) == 0 or len(s) == 0 or s is None or p is None):
            return result

        hashMap = dict()
        
        for char in p:
            hashMap[char] = hashMap.get(char, 0) + 1
        j = 0
        match_chars = 0

        for i in range(0, len(s)):
            incoming = s[i]
            if incoming in hashMap.keys():
                cnt = hashMap.get(incoming)
                cnt -= 1
                hashMap[incoming] = cnt
                if cnt == 0:
                    match_chars += 1

            
            if i >= len(p):
                outgoing = s[i - len(p)]
                if outgoing in hashMap.keys():
                    cnt = hashMap.get(outgoing)
                    cnt += 1
                    hashMap[outgoing] = cnt
                    if cnt == 1:
                        match_chars -= 1

            if len(hashMap) == match_chars:
                result.append(i - len(p) + 1)           
        
        return result

# // Sliding Window
# // Time Complexity:O(m+n)
# //Space Complexity: O(1)
