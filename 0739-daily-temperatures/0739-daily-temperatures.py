class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if temperatures is None or len(temperatures) == 0:
            return [0]

        n = len(temperatures)
        result = [0 for i in range(n)]
        st = []

        for index in range(n):
            while len(st) > 0 and temperatures[index] > temperatures[st[-1]]:
                top = st.pop(-1)
                result[top] = index - top
            
            st.append(index)
        
        return result