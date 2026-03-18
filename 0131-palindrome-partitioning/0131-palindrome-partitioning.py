class Solution:
    result = []
    def partition(self, s: str) -> List[List[str]]:
        self.result = list()
        if s is None or len(s) == 0:
            return self.result

        self.helper(s, list())
        return self.result
    
    def helper(self, s, path):
        if len(s) == 0:
            self.result.append(path.copy())
        
        for i in range(0, len(s)):
            if self.isPalindrome(s, 0, i):
                path.append(s[0 : i + 1])
                self.helper(s[i+1:], path)
                path.pop(-1)

    def isPalindrome(self, s, start, end):

        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        
        return True

# Substring For loop backtrack recursion
# Time Complexity: O(n * 2^n)
# Space Complexity: O()