class Solution:
    i = 0
    def decodeString(self, s: str) -> str:
        
        numSt = []
        strSt = []
        # strSt.append("")
        curr = [""]
        i = 0
        num = 0
        # result = ""

        for i in range(len(s)):
            char = s[i]
            # i += 1
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                # print(num)
                numSt.append(num)
                strSt.append("".join(curr))
                curr = [""]
                num = 0
                # print(numSt, strSt)
            elif char == "]":
                newStr = []
                times = numSt.pop()
                # print(times)
                for i in range(times):
                    newStr.append("".join(curr))  
                curr = [strSt.pop() + "".join(newStr)]
            else:
                curr.append(char)
            
            i += 1

        
        return "".join(curr)





