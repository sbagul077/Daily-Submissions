class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) < 3:
            return []
        
        result = list()
        n = len(nums)
        nums.sort()
        print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] >  0:
                break
            low, high = i + 1, n - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                
                if s == 0:
                    li = [nums[i], nums[low], nums[high]]
                    result.append(li)
                    low += 1
                    high -= 1
                    
                    while low < high and  nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif s < 0:
                    low += 1
                else:
                    high -= 1
                    
        return result
            