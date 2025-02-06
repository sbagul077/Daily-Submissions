class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = list()

        if arr is None or len(arr) == 0:
            return result
        
        low = 0
        high = len(arr) - k

        while low < high:
            mid = low + (high - low) // 2

            distS = x - arr[mid]
            distE = arr[mid + k] - x
            if distS > distE:
                low = mid + 1
            else:
                high = mid
        
        return arr[low: low + k]
# Binary Search
# TC =O(log(n - k)).
# Space complexity : O(1)