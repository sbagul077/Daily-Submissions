class Solution:
    result = list()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = list()

        if candidates is None or len(candidates) == 0:
            return self.result
        
        self.helper(candidates, 0, target, path = list())

        return self.result
    
    def helper(self, candidates: List[int], index: int, target: int, path: List[int]) -> None:
        #base
        if target == 0:
            self.result.append(path.copy())
            return
        
        if target < 0:
            return 

        #logic
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, i, target - candidates[i], path)
            path.pop(-1)

#Backtrack For Loop recursion
# Time Complexity:
# O(n * 2^(m+n)) where m is the candidates length and n is the target

# Space Complexity:
# O(n * h) -> O(n^2)
