from typing import List
import re


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_num(token: str):
            return bool(re.match("[-+]?\d+$", token))

        stack = []

        while tokens:
            token = tokens.pop()
            if is_num(token):
                result = int(token)
                while stack and type(stack[-1]) == int:
                    operand = stack.pop()
                    operator = stack.pop()

                    if operator == "+":
                        result += operand
                    elif operator == "-":
                        result -= operand
                    elif operator == "*":
                        result *= operand
                    else:
                        result = int(result / operand)
                stack.append(result)
            else:
                stack.append(token)

        return stack[-1]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*"]))
