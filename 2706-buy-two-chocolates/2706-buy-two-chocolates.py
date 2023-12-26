class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_1 = float("inf")
        min_2 = float("inf")
        
        for price in prices:
            if price < min_1:
                min_1, min_2 = price, min_1
            elif price < min_2:
                min_2 = price
        
        remaining = money - min_1 - min_2
        
        return remaining if remaining >= 0 else money

#time complexity: O(n)
#Space Complexity: O(1). No extra space
