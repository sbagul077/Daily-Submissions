class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""

        # numSt = []
        # charSt = []
        nums = 0
        result = [""]
        
        for char in s:

            if char.isdigit():
                nums = nums * 10 + (int(char))

            elif char == "[":
                result.append(nums)
                result.append("")
                nums = 0

            elif char == "]":
                # print(numSt,charSt,i)
                strSt = result.pop()
                times = result.pop()
            
                result[-1] += strSt * times
            else:
                result[-1] += char
        # print(result)
        return "".join(result)

