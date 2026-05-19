class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        openers = matches.values()

        for char in s:
            if char in openers:
                stack.append(char)
            elif stack:
                opener = stack.pop()
                if opener != matches[char]:
                    return False
            else:
                return False

        if stack != []:
            return False

        return True