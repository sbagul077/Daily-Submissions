class Solution:
    denominations = ["","Hundred", "Thousand", "Million","Billion", "Trillion"]
    tens = ["Zero", "Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    below_twenty = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten","Eleven",    
    "Twelve",  "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        self.denominations = [" ", "Thousand ", "Million ","Billion ", "Trillion "]
        self.tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.below_twenty = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten","Eleven",    
    "Twelve",  "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        result = ""
        denomination = 0
        while num > 0:
            if num % 1000 > 0:
                temp = self.helper(num % 1000) 
                print(temp, "temp")
                result = temp +  self.denominations[denomination] + result
                print(result, "result")
            denomination += 1
            num = num // 1000
        
        return result.strip()
    
    def helper(self, num : int) -> str:
        if num == 0:
            return ""
        if num < 20:
            return self.below_twenty[num] + " "
        elif(num < 100):
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.below_twenty[num // 100] + " Hundred " + self.helper(num % 100)