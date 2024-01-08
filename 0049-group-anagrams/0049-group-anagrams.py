class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams= dict()
        
        for s in strs:
            curr = self.primeProduct(s)
            
            if curr in anagrams:
                anagrams[curr].append(s)
            else:
                anagrams[curr] = [s]
        
        return anagrams.values()
    
    def primeProduct(self, s : str) -> float:
        result = 1
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        
        for i in range(len(s)):
            char = s[i]
            
            result *= primes[ord(char) - ord("a")]
        
        return result
        

