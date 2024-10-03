class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        n = len(nums)
        # if n == 1 and nums[0] == 
        
        index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                index = i
        # print(index)
        if nums[index] <=target <= nums[n - 1]:
            low = index
            high = n - 1
        else:
            low = 0
            high = index - 1

        # print(low, high)
        while low <= high:
            mid = low + (high - low)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low =  mid + 1
            else:
                high = mid - 1
        
        return -1
            
        