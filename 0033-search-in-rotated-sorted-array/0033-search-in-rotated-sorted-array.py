class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            #left side check
            if nums[low] <= nums[mid]:
                if nums[low] <= target<= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            #right side check
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1
