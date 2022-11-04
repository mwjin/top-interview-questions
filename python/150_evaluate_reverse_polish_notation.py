from typing import List
import re


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token = tokens.pop()
        if re.match("[-+]?\d+$", token):
            return int(token)
        else:
            right = self.evalRPN(tokens)
            left = self.evalRPN(tokens)

            if token == "+":
                return left + right
            elif token == "-":
                return left - right
            elif token == "*":
                return left * right
            else:
                return int(left / right)


# print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
# print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*"]))
