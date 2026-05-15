class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for char in s:
            if char.isalnum():
                new_s += char.lower()
        s = new_s

        p1 = 0
        p2 = len(s) - 1

        while p1 <= p2:

            if s[p1] != s[p2]:
                return False

            p1 += 1
            p2 -= 1

        return True