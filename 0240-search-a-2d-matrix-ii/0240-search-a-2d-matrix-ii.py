class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        
        while i < len(matrix) and j >= 0:
            curr = matrix[i][j]
            
            if curr == target:
                return True
            elif curr > target:
                j -= 1
            elif curr < target:
                i += 1
        
        return False

#Two Pointers
# TC: O(m) + O(n)
# SC: O(1)