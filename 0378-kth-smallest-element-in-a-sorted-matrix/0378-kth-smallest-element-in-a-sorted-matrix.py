class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]
        n = len(matrix)

        while low < high:
            mid = low + (high - low) // 2
            count = self.counter(matrix, mid, n)

            if count < k:
                low = mid + 1
            else:
                high = mid
        
        return low
    
    def counter(self, matrix, mid, n):
        count = 0

        for i in range(n):
            j = n - 1
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += j + 1
        
        return count