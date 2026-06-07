class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashMap = dict()

        #freq map of characters in t
        for i in t:
            hashMap[i] = hashMap.get(i, 0) + 1
        
        mapCount = dict() #keep count of no. of elements in the window
        left = 0
        right = 0
            #size start end
        result = [-1,0, 0]
        formed = 0
        while right < len(s):
            curr = s[right]
            mapCount[curr] = mapCount.get(curr, 0) + 1
            if curr in hashMap.keys() and hashMap.get(curr) >= mapCount.get(curr):
                formed += 1
                
            while formed == len(t) and left <= right:
                if result[0] == -1 or result[0] > (right - left):
                    result[0] = right-left + 1
                    result[1] = left
                    result[2] = right

                mapCount[s[left]] = mapCount.get(s[left]) - 1
            
                if s[left] in hashMap.keys() and mapCount.get(s[left]) < hashMap.get(s[left]): 
                    formed -= 1
                left += 1
            right += 1

        if result[0] == -1:
            return ""
        return s[result[1]: result[2] + 1]

# Two Pointers
#Time Complexity: O(n)
#Space Complexity:O(1)