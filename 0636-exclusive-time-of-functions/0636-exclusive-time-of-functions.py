class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0 for i in range(n)]
        st = []
        curr = 0
        prev = 0 
        
        if n is None:
            return result        
        
        for i in range(len(logs)):
            l = logs[i].split(":")
            curr = int(l[-1])            
            if l[1] == "start":
                if st:                    
                    temp = st[-1]
                    # print(temp)
                    result[temp] += curr - prev
                prev = curr
                st.append(int(l[0]))
            elif l[1] == "end":
                if st:
                    temp = st.pop()
                    result[temp] += (curr + 1) - prev
                prev = curr + 1
                
        return result
                    