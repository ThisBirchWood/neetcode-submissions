import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            try:
                stack.append(int(val))
                continue
            except ValueError:
                pass

            val2 = stack.pop()
            val1 = stack.pop()
            if val == "+":
                stack.append(val1 + val2)
            elif val == "-":
                stack.append(val1 - val2)
            elif val == "*":
                stack.append(val1 * val2)
            else:
                stack.append(int(val1 / val2))

        return stack[0]

