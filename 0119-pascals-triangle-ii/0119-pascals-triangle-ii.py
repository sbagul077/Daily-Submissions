class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        
        for i in range(rowIndex):
            newRow = [0] * (len(result) + 1)
            
            for j in range(len(result)):
                newRow[j] += result[j]
                newRow[j + 1] = result[j]
            
            result = newRow
        
        return result

#Time Complexity: O(n)
#Space Complexity: O(1)
                
            
            