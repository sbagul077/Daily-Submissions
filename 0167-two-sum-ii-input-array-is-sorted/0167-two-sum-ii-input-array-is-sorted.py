class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        
        while low <= high:
            currSum = numbers[high] +  numbers[low]
            
            if currSum == target:
                return [low + 1, high + 1]
            elif currSum > target:
                high -= 1
            else:
                low += 1
        
        return []
    
#Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(1)