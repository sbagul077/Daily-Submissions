class Solution:
    def binarySearch(self, matrix, target, start, vertical):
        low = start
        high = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if vertical:  # searching column
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:   #searching row
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True
        
        return False



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binarySearch(matrix, target, i, True)

            horizontal_found = self.binarySearch(matrix, target, i, False)

            if vertical_found or horizontal_found:
                return True
        
        return False