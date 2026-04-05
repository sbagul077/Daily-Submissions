class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if nums is None or len(nums) == 0 or len(nums) < k:
            return 0
        nums.sort()

        return nums[-k]