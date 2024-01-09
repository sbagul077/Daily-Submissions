class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        
        for s in strs:
            curr = self.primeProduct(s)
            
            if curr in hashMap.keys():
                hashMap[curr].append(s)
            else:
                hashMap[curr] = [s]
        
        return hashMap.values()
    

    def primeProduct(self, s):
        result = 1
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        
        for char in s:
            result *= primes[ord(char) - ord('a')]
        
        return result
