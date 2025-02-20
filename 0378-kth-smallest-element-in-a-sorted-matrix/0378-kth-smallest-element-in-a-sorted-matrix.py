import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li = list()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(li, matrix[i][j])

        i = 0
        while i != k - 1:
            heapq.heappop(li)
            i += 1
        
        return heapq.heappop(li)