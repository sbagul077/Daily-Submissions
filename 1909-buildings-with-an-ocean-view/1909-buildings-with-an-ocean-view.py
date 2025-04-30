class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if heights is None or len(heights) == 0:
            return []

        result = []
        n = len(heights)
        result.append(n-1)
        
        tallBuilding = heights[-1]

        for i in range(n-2, -1,-1): 
            curr = heights[i]
            if curr > tallBuilding:
                tallBuilding = curr
                result.append(i)
        
        result.sort()

        return result
