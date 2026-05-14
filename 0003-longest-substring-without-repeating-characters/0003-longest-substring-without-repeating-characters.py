class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = dict()

        slow = 0
        n = len(s)
        result = 0

        for fast in range(n):
            curr = s[fast]

            if curr in hashMap.keys():
                slow = max(slow, hashMap.get(curr))
            
            result = max(result, fast - slow + 1)
            hashMap[curr] = fast + 1
        

        return result

# // Sliding window
# // Time Complexity: O(n)
# // Space Complexity: O(1)