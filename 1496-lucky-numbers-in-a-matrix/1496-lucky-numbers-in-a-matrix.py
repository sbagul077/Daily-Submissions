class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or matrix is None:
            return []
        
        result = []

        for i in range(len(matrix)):
            minElement = min(matrix[i])
            index = 0
            for k in range(len(matrix[i])):
                if matrix[i][k] == minElement:
                    index = k
            j = 0
            # print(matrix[i][index] )
            while j < len(matrix):
                # print(matrix[i][index], matrix[j][index] )
                if matrix[i][index] < matrix[j][index]:
                    break
                j += 1     
                if j == len(matrix):
                    result.append(matrix[i][index])

        return result
            
                
            


                

