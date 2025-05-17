class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # [3,6,4,7,5,3,2]
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        # print(i)
        j = n - 1
        if i >= 0:
            while j > i and nums[j] <= nums[i]:
                j -= 1
            print(j)
            self.swap(nums, i, j)    
        self.reverse(nums, i + 1)
    

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def reverse(self, nums, left):
        right = len(nums) - 1

        while left <= right:
            self.swap(nums, left, right)
            left += 1
            right -= 1



