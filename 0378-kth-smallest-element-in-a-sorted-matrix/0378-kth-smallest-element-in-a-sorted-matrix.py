class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li = list()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                li.append(matrix[i][j])
        li.sort()
        return li[k-1]