class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stripped = ''
        for char in s:
            if char.isalnum() and char != " ":
                s_stripped += char.lower().strip()
        s_b = ''
        for i in range(len(s_stripped)-1, -1, -1):
            s_b += s_stripped[i]
        if s_stripped == s_b: return True
        return False