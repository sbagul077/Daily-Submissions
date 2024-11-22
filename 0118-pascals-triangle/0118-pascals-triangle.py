class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == None:
            return []
        
        result = []
        
        for row in range(0, numRows):
            li = list()
            for col in range(0, row + 1):
                if col == 0 or col == row:
                    li.append(1)
                else:                    
                    curr = result[row - 1]
                    left = curr[col - 1]
                    right = curr[col]                    
                    li.append(left + right)            
            result.append(li)
        
        return result
                
                
            
            
            