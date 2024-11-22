class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashMap = dict()
        
        for i in matrix:
            
            row_pattern = "".join("T" if num == i[0] else "F" for num in i)
            
            hashMap[row_pattern] = (hashMap.get(row_pattern, 0) + 1)
        
        return max(hashMap.values(), default = 0)
            