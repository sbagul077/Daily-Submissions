class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None or len(strs) == 0:
            return [[""]]
        
        hashMap = dict()
        
        for i in range(len(strs)):
            curr = ''.join(sorted(strs[i]))
            # print(curr)
            if curr in hashMap.keys():
                hashMap.get(curr).append(strs[i])
            else:
                # print(curr, hashMap)
                hashMap[curr] = [strs[i]]
        
        
        return hashMap.values()
    
#hashing
#Time Complexity: O(nklogk)
#Space Complexity: O(n)