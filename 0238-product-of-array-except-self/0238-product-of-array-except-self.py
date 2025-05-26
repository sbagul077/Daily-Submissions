class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return list()
        
        rp = 1
        arr = [1 for i in range(len(nums))]


        for i in range(1, len(nums)):
            arr[i] = rp * nums[i - 1]
            rp = arr[i]
        
        # print(arrLHS)
        rp = 1
        for i in range(len(nums) - 2, -1, -1):
            arr[i] = arr[i] * rp * nums[i + 1]
            rp = rp * nums[i + 1]
        return arr

#Time Complexity: O(m+n)
#Space complexity: O(m + m)
