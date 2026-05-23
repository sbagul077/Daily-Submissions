class Solution:
    def calculate(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        
        # tail = 0
        curr = 0
        calc = 0
        # s.strip()

        lastSign = '+'
        st = []

        for i in range(len(s)):
            ch = s[i]

            if ch.isnumeric():
                curr = curr * 10 + int(ch)
            
            if(not ch.isdigit() and ch != " ") or i == len(s) - 1:
                if lastSign == "+":
                    st.append(curr)
                elif lastSign == "-":
                    st.append(-curr)
                elif lastSign == "*":                    
                    st.append(st.pop() * curr)
                elif lastSign == "/":
                    st.append(int(st.pop() / curr))
                
                curr = 0
                lastSign = ch
        
        while len(st) > 0:
            calc += st.pop()
        return calc

# Time Complexity: O(n)
# Space Complexity: O(n)