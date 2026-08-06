class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        seen = {}
        
        for r, char in enumerate(s):
            window = r - l + 1

            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

            if window - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            else:
                res = max(res, window)

        return res

            

            
    