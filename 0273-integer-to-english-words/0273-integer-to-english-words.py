class Solution:
    tens = []
    below_20 = []
    # result = []
    def numberToWords(self, num: int) -> str:
        self.tens = ["","Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty","Seventy", "Eighty", "Ninety"]
        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
        "Thirteen", "Fourteen","Fifteen", "Sixteen", "Seventeen","Eighteen", "Nineteen"]
        result = ""
        i = 0
        thousands = [" ", "Thousand ", "Million ", "Billion ", "Trillion "]

        if num == 0:
            return "Zero"

        while num > 0:
            # num = num // 1000
            if num % 1000 > 0:
                result = self.helper(num % 1000) + thousands[i] + result
            i += 1
            num = num // 1000
        
        return result.strip()
    
    def helper(self, num):

        if num == 0:
            return ""
        
        if num < 20:
            return self.below_20[num] + " "

        elif num < 100:
            # print(num // 10, num % 10)
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            # print(num // 100, num % 100)
            return self.below_20[num // 100] + " Hundred " + self.helper(num % 100)

        
