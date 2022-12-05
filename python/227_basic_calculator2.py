from typing import List
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        s = "".join(s.split())
        rpn = deque()

        def findOp(start: int, end: int) -> int:
            for i in range(end - 1, start - 1, -1):
                if s[i] == "+" or s[i] == "-":
                    return i

            for i in range(end - 1, start - 1, -1):
                if s[i] == "*" or s[i] == "/":
                    return i

            return -1

        def createRPN(start: int, end: int):
            op_idx = findOp(start, end)

            if op_idx == -1:
                rpn.appendleft(s[start:end])
                return

            rpn.appendleft(s[op_idx])
            createRPN(op_idx + 1, end)
            createRPN(start, op_idx)

        createRPN(0, len(s))
        return self.evalRPN(rpn)

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


print(Solution().calculate("1+2*5/3+6/4*2"))
