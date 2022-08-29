from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def pushParenthesis(path=[], numLeft=0):
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            if numLeft < n:
                path.append("(")
                pushParenthesis(path, numLeft + 1)
                path.pop()

            if len(path) - numLeft < numLeft:
                path.append(")")
                pushParenthesis(path, numLeft)
                path.pop()

        pushParenthesis()
        return result


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))
