class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        
        while i >= 0 and j <= len(matrix[0]) - 1:
            curr = matrix[i][j]
            
            if curr == target:
                return True
            elif curr > target:
                i -= 1
            elif curr < target:
                j += 1
        
        return False

#Two Pointers
# TC: O(m) + O(n)
# SC: O(1)