class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        return n > 0 and log(n, 4) % 1 == 0
            # return True
        
        if n == 1:
            return True
        
        if n <= 0 or n % 4:
            return False
        
        return self.isPowerOfFour(n // 4)

    
#Recursion and Maths(logarithmic)
#Time Complexity: O(n)
#Space Complexity: O(1)