class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append(list())

        for i in range(len(nums)):
            size = len(result)
            for k in range(size):
                tempList = list(result[k])
                tempList.append(nums[i])
                result.append(tempList)
        
        return result

#For Loop
