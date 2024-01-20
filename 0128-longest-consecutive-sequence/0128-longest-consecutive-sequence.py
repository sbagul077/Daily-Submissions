class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        self.max = 0
        
        
        for num in nums:
            if (num - 1) not in hashSet:
                # print(num, num - 1)
                currLen = 0
                while (num + currLen) in hashSet:
                    currLen += 1
                self.max = max(self.max, currLen)
        
        return self.max
                