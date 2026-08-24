class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return 
        
        n = len(nums)
        if k > n:
            k = k % n
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):

        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
    
    def swap(self, nums, start, end):
        nums[start], nums[end] = nums[end], nums[start]

# Time Complixty: O(3n)
# Space Complexity: O(1)