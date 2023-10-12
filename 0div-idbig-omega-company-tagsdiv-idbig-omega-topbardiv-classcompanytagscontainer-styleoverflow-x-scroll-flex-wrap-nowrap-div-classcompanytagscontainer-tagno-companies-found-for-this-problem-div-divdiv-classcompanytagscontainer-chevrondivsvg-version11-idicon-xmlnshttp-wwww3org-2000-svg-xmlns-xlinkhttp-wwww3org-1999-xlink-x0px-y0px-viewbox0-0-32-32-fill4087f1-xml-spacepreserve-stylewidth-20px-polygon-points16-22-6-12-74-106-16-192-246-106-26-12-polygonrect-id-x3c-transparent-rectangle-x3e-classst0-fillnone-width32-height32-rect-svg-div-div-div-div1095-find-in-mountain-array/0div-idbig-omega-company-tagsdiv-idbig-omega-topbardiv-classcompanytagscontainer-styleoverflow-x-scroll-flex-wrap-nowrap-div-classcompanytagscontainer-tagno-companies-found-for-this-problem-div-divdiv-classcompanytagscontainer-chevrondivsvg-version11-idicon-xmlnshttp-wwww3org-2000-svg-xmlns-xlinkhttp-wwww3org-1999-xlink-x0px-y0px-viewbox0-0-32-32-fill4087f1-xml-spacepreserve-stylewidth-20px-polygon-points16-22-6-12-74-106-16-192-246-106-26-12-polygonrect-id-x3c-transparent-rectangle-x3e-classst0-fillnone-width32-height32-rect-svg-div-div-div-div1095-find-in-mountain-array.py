# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        
        low = 1
        high = length - 2 # we take one less on left and one left on right as we won't find any peak on the edges, slight optimization
        mid = 0
        while low <= high:
            mid = low + (high - low) // 2
            
            left = mountain_arr.get(mid - 1)
            middle = mountain_arr.get(mid)
            right = mountain_arr.get(mid + 1)
        
            if left < middle < right:
                low = mid + 1            
            elif left > middle > right:
                high = mid - 1            
            else:
                break
            
        peak = mid
        # print(mountain_arr.get(mid))
        #search on left side of the array
        low = 0
        high = peak
        
        while low <= high:
            mid = low + (high - low) // 2
            
            val = mountain_arr.get(mid)
            
            if val == target:
                return mid
            elif val > target:
                high = mid - 1
            else:
                low = mid + 1
        
        #searh on the right side of the array
        
        low = peak  
        high = length - 1
        # print(mountain_arr.get(low), mountain_arr.get(high))
        while low <= high:
            
            mid = low + (high - low) // 2
            
            val = mountain_arr.get(mid)
            print(val)
            if val == target:
                return mid
            elif val > target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

#Binary Search
#Time Complexity: O(2logn)
#Space Complexity: O(1)
            
            