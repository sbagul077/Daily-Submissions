class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        
        st = []

        for i in range(len(s)):
            char = s[i]

            if char == "{":
                st.append("}")
            elif char == "[":
                st.append("]")
            elif char == "(":
                st.append(")")
            elif len(st) == 0 or st.pop() != char:
                return False
        
        
        return len(st) == 0
            