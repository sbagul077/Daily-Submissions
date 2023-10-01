class Solution:
    def reverseWords(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s
        
        s = list(s)
        left = 0
        
        for right in range(len(s)): 
            
            if s[right] == " " or right == len(s) - 1:    
                temp_left = left
                temp_right = right - 1
                
                if right == len(s) - 1:
                    temp_right = right
                    
                while temp_left < temp_right:
                    s[temp_left], s[temp_right] = s[temp_right], s[temp_left]
                    
                    temp_left += 1
                    temp_right -= 1
                    
                left = right + 1
            
        return "".join(s)
        
#Two Pointers 
#Time Complexity: O(n)
#Space Complexity: O(1)