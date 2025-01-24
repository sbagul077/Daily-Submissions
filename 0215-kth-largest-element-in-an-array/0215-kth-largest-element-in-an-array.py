class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = list()

        for num in nums:
            pq.append([-num, num])
        
        heapq.heapify(pq)

        for i in range(k - 1):
            heapq.heappop(pq)
        
        return heapq.heappop(pq)[1]