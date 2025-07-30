class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        if temperatures is None or len(temperatures) == 0:
            return result
        
        st = []

        for index in range(len(temperatures)):
            while st and temperatures[index] > temperatures[st[-1]]:
                top = st.pop()
                result[top] = index - top
            st.append(index)
        return result
    
#Time complexity: O(n)
#Space Complexity: O(n)