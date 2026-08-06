class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        l = 0

        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1

        for r, char in enumerate(s2):
            freq[char] = freq.get(char, 0) + 1

            # Frequencies match, it is a permutation
            if freq == s1_freq:
                return True

            if s2[l] not in s1_freq or r - l + 1 >= len(s1):
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0:
                    del freq[s2[l]]
                l += 1

        return False
