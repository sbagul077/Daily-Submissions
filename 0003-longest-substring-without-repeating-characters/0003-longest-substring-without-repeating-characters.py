class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        slow = 0
        maximum = 0
        for i in range(len(s)):
            c = s[i]
            # print(m)
            if c in m.keys():
                slow = max(slow, m.get(c))
            maximum = max(maximum, i - slow + 1)
            m[c] = i + 1
        return maximum
            