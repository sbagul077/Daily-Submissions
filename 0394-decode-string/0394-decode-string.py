class Solution:
    i = 0
    def decodeString(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""
        
        num = 0
        curr = [""]

        while self.i < len(s):
            char = s[self.i]
            if char.isdigit():
                num = num * 10 + int (char)
                self.i += 1
            elif char == '[':
                self.i += 1
                decoded = self.decodeString(s)
                newStr = []
                for k in range(num):
                    newStr.append(decoded)
                curr.append("".join(newStr))
                num = 0
            elif char == "]":
                self.i += 1
                return "".join(curr)
            else:
                curr.append(char)
                self.i += 1
        
        return "".join(curr)
            


