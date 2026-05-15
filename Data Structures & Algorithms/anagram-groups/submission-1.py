class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_words = {}
        for word in strs:
            current_letters = {}
            for char in word:
                if char in current_letters:
                    current_letters[char] += 1
                else:
                    current_letters[char] = 1
            
            dict_set = set()
            for key in current_letters:
                dict_set.add((key, current_letters[key]))
            current_letters = tuple(sorted(dict_set, key=lambda x: x[0]))

            if current_letters in dict_words:
                dict_words[current_letters].append(word)
            else:
                dict_words[current_letters] = [word]
            
        return dict_words.values()
            