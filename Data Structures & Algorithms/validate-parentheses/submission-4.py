class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = False

        if len(s) <= 1:
            return False

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                open_bracket = stack.pop()
                if open_bracket == "(" and char != ")":
                    return False
                elif open_bracket == "[" and char != "]":
                    return False
                elif open_bracket == "{" and char != "}":
                    return False

        if len(stack) != 0:
            return False

        return True

                