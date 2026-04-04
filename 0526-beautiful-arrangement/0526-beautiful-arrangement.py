class Solution:
    count = 0
    arr = list()
    def countArrangement(self, n: int) -> int:
        self.count = 0

        if n is None or n == 0:
            return self.count
        
        self.arr = [i + 1 for i in range(n)]
        
        self.dfs(0, self.arr, len(self.arr))
        return self.count
    
    def dfs(self, pivot, arr, n):
        #base
        if pivot == n:
            self.count += 1
        
        for i in range(pivot, n):
            arr[i], arr[pivot] = arr[pivot], arr[i]

            if arr[pivot] % (pivot + 1) == 0 or (pivot + 1) % arr[pivot] == 0:
                self.dfs(pivot + 1, arr, n)

            arr[i], arr[pivot] = arr[pivot], arr[i]
        
