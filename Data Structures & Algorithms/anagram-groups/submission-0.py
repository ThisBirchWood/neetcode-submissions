class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dict_chars = []


        for s in strs:
            words = {}
            for char in s:
                if char in words:
                    words[char] += 1
                else:
                    words[char] = 1

            if words in dict_chars:
                index = dict_chars.index(words)
                result[index].append(s)
            else:
                dict_chars.append(words)
                result.append([s])
        return result
            

        


            
            