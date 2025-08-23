class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None or len(strs) == 0:
            return []
        
        hashMap = dict()

        for str in strs:
            primeProduct = self.getPrimeProduct(str)

            if(primeProduct not in hashMap.keys()):
                hashMap[primeProduct] = list()
            
            hashMap.get(primeProduct).append(str)
        # print(hashMap)
        return list(hashMap.values())
    
    def getPrimeProduct(self, word):

        result = 1

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103]
        
        for char in word:
            result = result * primes[ord(char) - ord("a")]

        return result