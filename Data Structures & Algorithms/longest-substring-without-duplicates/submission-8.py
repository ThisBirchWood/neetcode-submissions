class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        seen = {}

        while r < len(s):
            char = s[r]
            
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            
            seen[char] = r
            res = max(res, r - l + 1)
            r += 1

        return res
