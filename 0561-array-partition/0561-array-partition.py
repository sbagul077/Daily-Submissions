class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        maxSum = 0 

        for i in range(0, len(nums), 2):
            maxSum += nums[i]
        
        return maxSum

# Sorting and skipping even numbers
#time Complexity: O(nlogn)
# Space Complexity: O(1)