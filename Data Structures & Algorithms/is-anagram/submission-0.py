class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars_s = {}
        chars_t = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in chars_s:
                chars_s[s_char] += 1
            else:
                chars_s[s_char] = 1

            if t_char in chars_t:
                chars_t[t_char] += 1
            else:
                chars_t[t_char] = 1

        if chars_s == chars_t:
            return True
        return False

