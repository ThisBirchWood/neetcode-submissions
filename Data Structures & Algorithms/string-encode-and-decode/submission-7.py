class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            i = j

            res.append(s[i+1 : i+1+length])
            i += length + 1

        return res
