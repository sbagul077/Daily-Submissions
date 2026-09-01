class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n - 2 
        while i >= 0:
            if nums[i] < nums[i + 1]:
                for j in range(n-1, i, -1):
                    
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        # print(nums)
                        break
                
                break
            i -= 1
        
        self.reverse(nums, i + 1, n - 1)            
    
    def reverse(self,nums, start, end):
        
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
