class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {}
        word_2 = {}

        for x in s:
            if x in word_1:
                word_1[x] += 1
            else:
                word_1[x] = 1

        for x in t:
            if x in word_2:
                word_2[x] += 1
            else:
                word_2[x] = 1

        if word_1 == word_2:
            return True
        return False