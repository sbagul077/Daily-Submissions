class Solution:
    def jump(self, nums: list[int]) -> int:
        if nums is None or len(nums) < 2:
            return 0
        nextInt = nums[0]
        currInt = nums[0]
        jumps = 1
        for i in range(1, len(nums) - 1):
            nextInt = max(nextInt, nums[i] + i)

            if i == currInt:
                jumps += 1
                currInt = nextInt
        
        return jumps