class Solution:
    def calculate(self, s: str) -> int:
        st = []
        calc = 0 
        curr = 0
        lastSign = "+"

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                curr = curr * 10 + int(char)
            
            if (not char.isdigit() and char != " ") or (i == len(s) - 1):
                if lastSign == "+":
                    st.append(curr)
                elif lastSign == "-":
                    st.append(-curr)
                elif lastSign == "*":
                    st.append(st.pop() * curr)
                elif lastSign == "/":
                    st.append(int(st.pop() / curr))
                
                lastSign = char
                curr = 0
        
        while len(st) > 0:
            calc += st.pop()
        
        return calc
# // Stack
# // Time Complexity: O(n)
# // Space Complexity: O(n)
