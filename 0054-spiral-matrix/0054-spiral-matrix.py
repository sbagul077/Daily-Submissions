class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list() # return answer
        
        m = len(matrix)
        n = len(matrix[0])
        
        top = 0
        bottom = m - 1
        
        left = 0
        right = n - 1
        
        while left <= right and bottom >= top:
            #top
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            #right
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1 
            
            if top <= bottom:
                for col in range(right, left -1, -1):                
                    result.append(matrix[bottom][col])                
                bottom -= 1       
            
            if left <= right:
                for i in range(bottom , top - 1, -1):
                    result.append(matrix[i][left])
                left += 1 
                       
        return result
            
            
            