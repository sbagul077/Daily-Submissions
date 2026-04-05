import heapq

class Solution:
    def findKthLargest(self, nums, k):
        pq = []
        n = len(nums)
        result = float("inf")
        for i in range(n):
            heapq.heappush(pq, -nums[i])

            if len(pq) > n-k:
                result = min(result, -heapq.heappop(pq))

        return result

# Max Heap
# time complexity: O(n log k)
# space complexity: O(k)