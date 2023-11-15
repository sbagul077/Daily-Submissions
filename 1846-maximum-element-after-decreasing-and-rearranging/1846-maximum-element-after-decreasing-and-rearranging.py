class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        
        for n in arr:
            if n >= prev + 1:
                prev += 1
        
        return prev
    
#Greedy
#Time Complexity: O(n.logn)
#Space Complexity: O(logn)