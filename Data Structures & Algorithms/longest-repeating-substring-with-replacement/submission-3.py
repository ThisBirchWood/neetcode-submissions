class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        seen = {}
        max_freq = 0
        
        for r, char in enumerate(s):
            window = r - l + 1
            seen[char] = seen.get(char, 0) + 1
            max_freq = max(max_freq, seen[char])

            if window - max_freq > k:
                seen[s[l]] -= 1
                l += 1
            else:
                res = max(res, window)

        return res

            

            
    