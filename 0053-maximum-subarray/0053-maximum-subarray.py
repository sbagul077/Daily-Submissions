class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        result = nums[0]

        rSum = nums[0]

        for i in range(1,len(nums)):

            rSum =  max(rSum + nums[i], nums[i])

            result = max(result, rSum)

        return result

#time complexity: O(n)
#space complexity: O(1)