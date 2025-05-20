class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1]

        n = len(nums)  #len of nums array
        result = [-1 for i in range(n)]
        st = [] #decreasing monotonic stack to index of the elements

        for index in range((n * 2)):
                
            currIndex = index % (n)
            # print(st, currIndex, nums[currIndex])
            # print(st, nums[currIndex] ,nums[st[-1]])
            while st and nums[currIndex] > nums[st[-1]]:
                top = st.pop(-1)
                result[top] = nums[currIndex]

            if index < n:
                st.append(index)
        
        return result