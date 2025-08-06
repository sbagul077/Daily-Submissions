class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        
        left = 0
        right = len(s) - 1

        while left <= right:
            charLeft = s[left]
            charRight = s[right]

            if not charLeft.isalpha() and not charLeft.isnumeric():
                left += 1
            elif not charRight.isalpha() and not charRight.isnumeric():
                right -= 1
            elif charLeft.lower() != charRight.lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True