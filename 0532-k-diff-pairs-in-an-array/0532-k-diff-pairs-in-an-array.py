class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        slow = 0
        n = len(nums)
        nums.sort()
        fast = 1
        while fast < n:
            curr = nums[fast] - nums[slow]
            if curr > k:
                slow += 1
            elif curr < k or fast == slow:
                fast += 1
            else:
                result += 1
                slow += 1
                fast += 1
                
                while fast < n and nums[fast] == nums[fast - 1]:
                    fast += 1

        return result
                    
            
            