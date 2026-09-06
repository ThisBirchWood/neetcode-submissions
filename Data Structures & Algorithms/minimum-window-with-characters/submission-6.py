class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        window = {}
        windowLen = float("infinity")
        res = [-1, -1]

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < windowLen:
                    res = [l, r]
                    windowLen = r - l + 1

                l_char = s[l]
                window[l_char] -= 1

                if l_char in countT and window[l_char] < countT[l_char]:
                    have -= 1
                
                l += 1
            

        l, r = res
        return s[l:r+1] if not windowLen == float("infinity") else ""

        
            

                    
