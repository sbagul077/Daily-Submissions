class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        left = 0
        
        for right in range(1, len(colors)):
            if colors[left] == colors[right]:
                if neededTime[left] > neededTime[right]:
                    result += neededTime[right]                    
                else:
                    result += neededTime[left]
                    left = right
            else:
                left = right
        
        return result
    

# Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(1)