class Solution:
    tens = []
    below_20 = []
    def numberToWords(self, num: int) -> str:       
        
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        self.below_20 = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        if num == 0:
            return self.below_20[0]
        
        thousands = [" ", "Thousand ", "Million ", "Billion ", "Trillion "]
        
        i = 0
        result = ""
        
        while num > 0:
            if num % 1000 != 0:         
                result =  self.helper(num % 1000) + thousands[i] + result            
            num = num // 1000
            i += 1        
        return result.strip()
    
    
    def helper(self, num):
        if num == 0:
            return ""
        
        if num < 20:
            return self.below_20[num] + " "
        
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.below_20[num //100] + " Hundred " + self.helper(num % 100)

# Recursion, Coding
# Time Complexity: O(1)
# Space Complexity: O(1)