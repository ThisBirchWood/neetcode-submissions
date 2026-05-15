class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''

        for word in strs:
            l = len(word)
            s += str(l) + "/" + word

        return s 

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        num = ''
        
        while i < len(s):

            if s[i] == '/':
                len_word = int(num)
                out.append(s[i+1:i+len_word+1])
                i += len_word + 1
                num = ''
            else:
                num += s[i]
                i += 1

        return out



            