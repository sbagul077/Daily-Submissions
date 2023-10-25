class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        low = 1
        high = 2**(n - 1)
        curr = 0
        
        for _ in range(n - 1):
            mid = low + (high - low) // 2
            
            if k <= mid:
                high = mid
            else:
                low = mid + 1
                curr = 0 if curr else 1
        
        return curr
    
    
#Binary Search
#Time Complexity: O(logn)
#Space Complexity: O(h). Height of the tree