from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opMap = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }

        for token in tokens:
            if token in opMap:
                rightOp = stack.pop()
                leftOp = stack.pop()
                stack.append(opMap[token](leftOp, rightOp))
            else:
                stack.append(int(token))

        return stack[-1]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*"]))
