class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = self.letters_in_string(s)
        word_2 = self.letters_in_string(t)

        if word_1 == word_2:
            return True
        return False

    def letters_in_string(self, string):
        letters = {}
        for x in string:
            if x in letters:
                letters[x] += 1
            else:
                letters[x] = 1
        return letters