class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return []


        hashMap = dict()

        for i in range(len(nums)):
            # print(hashMap)
            diff = target - nums[i]
            if diff in hashMap.keys():
                return [i, hashMap.get(diff)]
            else:
                hashMap[nums[i]] = i
        
        return []